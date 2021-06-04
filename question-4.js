/* Extracting countries from JSON */
function to_countries(country_population) {
    var data = JSON.parse(JSON.stringify(country_population));
    keys = Object.keys(data);
    /* Changing counter names to shorter ones */
    for (i = 0; i < keys.length; i++) {
        if (keys[i] == "Brunei Darussalam") {
            keys[i] = "Brunei"
        }
        if (keys[i] == "Lao People's Democratic Republic") {
            keys[i] = "Laos"
        }
    }
    return keys;
}

/* Extracting population data from JSON */
function to_population(country_population) {
    var data = JSON.parse(JSON.stringify(country_population));
    keys = Object.keys(data);
    values = Object.values(data);
    var converted_data = [];
    for (i = 0; i < keys.length; i++) {
        converted_data.push({ name: keys[i], data: values[i] });
    }
    return converted_data;
}

/* Years for x-axis labels */
years = [
         "2005", "2006", "2007",
         "2008", "2009", "2010",
         "2011", "2012", "2013", "2014"
        ];

/* url to fetch json location */
total_asean_url= '/datasets/json/total-asean-population.json';

$(document).ready(function () {
    fetch(total_asean_url).then((response) => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Something went wrong');
        }
    })
        .then((total_asean_responseJson) => {
            countries = to_countries(total_asean_responseJson); 
            population = to_population(total_asean_responseJson);
            Highcharts.chart('highchart-graph-4', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'TOTAL population of ASEAN countries'
                },
                subtitle: {
                    text: 'Source: <a href="https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv">World Population</a>'
                },
                xAxis: {
                    categories: years,
                    title: {
                        text: 'Years'
                    },
                    crosshair: true
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: 'Population'
                    }
                },
                tooltip: {
                    headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                    pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                        '<td style="padding:0"><b>{point.y}</b></td></tr>',
                    footerFormat: '</table>',
                    shared: true,
                    useHTML: true
                },
                plotOptions: {
                    column: {
                        pointPadding: 0.2,
                        borderWidth: 0
                    }
                },
                series: population
            });
        })
        .catch((error) => {
            console.log(error)
        });
});
