/* url to fetch json location */
asean_url = '/datasets/json/asean-population.json';

$(document).ready(function () {
    fetch(asean_url).then((response) => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Something went wrong');
        }
    })
        .then((asean_responseJson) => {
            Highcharts.chart('highchart-graph-2', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Population of ASEAN countries for the year 2014'
                },
                subtitle: {
                    text: 'Source: <a href="https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv">World Population</a>'
                },
                xAxis: {
                    title: {
                        text: 'Years'
                    },
                    type: 'category',
                    labels: {
                        rotation: -45,
                        style: {
                            fontSize: '13px',
                            fontFamily: 'Verdana, sans-serif'
                        }
                    }
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: 'Population'
                    }
                },
                legend: {
                    enabled: false
                },
                tooltip: {
                    pointFormat: 'Population in 2014: <b>{point.y}</b>'
                },
                series: [{
                    name: 'Population',
                    data: asean_responseJson,
                    dataLabels: {
                        enabled: true,
                        rotation: 0,
                        color: '#FFFFFF',
                        align: 'center',
                        format: '{point.y}', // one decimal
                        y: 10, // 10 pixels down from the top
                        style: {
                            fontSize: '13px',
                            fontFamily: 'Verdana, sans-serif'
                        }
                    }
                }]
            });
        })
        .catch((error) => {
            console.log(error)
        });
});
