"""
Generating JSON data files to plot graphs on Browser
"""
# importing the required libraries
import csv
from collections import defaultdict
import json
from sqlalchemy import Column, Float, String, create_engine, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.sql import func

Base = declarative_base()


class PopulationData(Base):
    """
    Defining table populationdata and its columns
    """
    __tablename__ = "populationdata"

    id = Column(Integer, primary_key=True)
    region = Column(String)
    year = Column(Integer)
    population = Column(Float)


class AseanCountries(Base):
    """
    Defining table aseancountries and its columns
    """
    __tablename__ = "aseancountries"

    id = Column(Integer, primary_key=True)
    country = Column(String)


class SaarcCountries(Base):
    """
    Defining table saarccountries and its columns
    """
    __tablename__ = "saarccountries"

    id = Column(Integer, primary_key=True)
    country = Column(String)


def total_population(session):
    """
    Adding data from csv to table PopulationData
    """
    with open('datasets/csv/population_estimates_csv.csv', 'r') as csv_file:
        csv_list = list(csv.DictReader(csv_file, delimiter=','))
        csv_file.close()

    for row in csv_list:
        session.add_all([
            PopulationData(region=row['Region'],
                           year=row['Year'], population=row['Population'])
        ])
    session.commit()


def asean_countries(session):
    """
    Adding data from csv to table AseanCountries
    """
    with open('datasets/csv/asean_countries.csv', 'r') as file:
        asean_list = [row['ASEAN-countries'] for row in csv.DictReader(file)]
        file.close()

    for row in asean_list:
        session.add_all([
            AseanCountries(country=row)
        ])
    session.commit()


def saarc_countries(session):
    """
    Adding data from csv to table SaarcCountries
    """
    with open('datasets/csv/saarc_countries.csv', 'r') as file:
        saarc_list = [row['SAARC-countries'] for row in csv.DictReader(file)]
        file.close()

    for row in saarc_list:
        session.add_all([
            SaarcCountries(country=row)
        ])
    session.commit()


def indian_population():
    """
    JSON data generation for Bar Plot of 'population of India' vs. years.
    """
    query1 = Session.query(PopulationData)\
                    .filter(PopulationData.region == 'India')\
                    .order_by(desc(PopulationData.year))\
                    .limit(10).offset(1)

    # formatting data accordingly
    data = [[row.year, int(float(row.population))] for row in query1]

    # duming data in JSON file
    with open('datasets/json/indian-population.json', 'w') as json_file:
        json.dump(data, json_file)


def asean_population():
    """
    JSON data generation for
    population of ASEAN countries for the year 2014
    """
    query2 = Session.query(PopulationData)\
                    .filter(PopulationData.region
                            .in_(Session.query(AseanCountries.country)))\
                    .filter(PopulationData.year == 2014)\
                    .order_by(PopulationData.region)

    asean_list = []
    population = []

    for row in query2:
        asean_list.append(row.region)
        population.append(int(float(row.population)))

    # changing names to shorter one's
    for key, value in enumerate(asean_list):
        if value == "Brunei Darussalam":
            asean_list[key] = "Brunei"
        elif value == "Lao People's Democratic Republic":
            asean_list[key] = "Laos"

    # formatting data accordingly
    data = [[country, pop] for country, pop in zip(asean_list, population)]

    # duming data in JSON file
    with open('datasets/json/asean-population.json', 'w') as json_file:
        json.dump(data, json_file)


def total_saarc_population():
    """
    JSON data generation for Total SAARC population vs year
    """

    query3 = Session.query(func.sum(PopulationData.population)
                           .label("population_sum"))\
                    .filter(PopulationData
                            .region.in_(Session
                                        .query(SaarcCountries.country)))\
                    .filter(PopulationData.year.between(2005, 2015))\
                    .group_by(PopulationData.year)\
                    .order_by(PopulationData.year)

    population = [int(float(row.population_sum)) for row in query3]

    # formatting data accordingly
    years = [
             "2005", "2006", "2007", "2008",
             "2009", "2010", "2011", "2012",
             "2013", "2014", "2015"
            ]
    data = [[year, pop] for year, pop in zip(years, population)]

    # duming data in JSON file
    with open('datasets/json/total-saarc-population.json', 'w') as json_file:
        json.dump(data, json_file)


def total_asean_population():
    """
    JSON data generation for ASEAN countries for the years 2005 to 2014
    """

    population = defaultdict(list)

    query4 = Session.query(PopulationData)\
                    .filter(PopulationData.region
                            .in_(Session.query(AseanCountries.country)))\
                    .filter(PopulationData.year.between(2005, 2014))

    for row in query4:
        population[row.region].append(int(float(row.population)))

    # duming data in JSON file
    with open('datasets/json/total-asean-population.json', 'w') as json_file:
        json.dump(population, json_file)


if __name__ == '__main__':

    # Connection URL
    PGURL = "postgresql://abcd:password1@localhost:5432/populationdata"

    # Creating engine and binding Session
    engine = create_engine(PGURL, echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)()

    # Checking if data exist in table PopulationData
    if Session.query(PopulationData).count():
        print("Data exists in Table PopulationData.")
    else:
        # dumping data into table
        total_population(Session)

    # Checking if data exist in table AseanCountries
    if Session.query(AseanCountries).count():
        print("Data exists in Table AseanCountries.")
    else:
        # dumping data into table
        asean_countries(Session)

    # Checking if data exist in table SaarcCountries
    if Session.query(SaarcCountries).count():
        print("Data exists in Table SaarcCountries.")
    else:
        # dumping data into table
        saarc_countries(Session)

    # Calling respective functions to generate JSON's
    indian_population()
    asean_population()
    total_saarc_population()
    total_asean_population()
