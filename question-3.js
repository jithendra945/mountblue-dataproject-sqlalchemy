/* url to fetch json location */
saarc_url = '/datasets/json/total-saarc-population.json';

$(document).ready(function () {
    fetch(saarc_url).then((response) => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Something went wrong');
        }
    })
        .then((saarc_responseJson) => {
            Highcharts.chart('highchart-graph-3', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'TOTAL population of SAARC countries'
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
                    pointFormat: 'Population : <b>{point.y}</b>'
                },
                series: [{
                    name: 'Population',
                    data: saarc_responseJson,
                    dataLabels: {
                        enabled: true,
                        rotation: -90,
                        color: '#FFFFFF',
                        align: 'right',
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
