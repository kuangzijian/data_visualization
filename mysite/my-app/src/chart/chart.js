import React from 'react';
import 'antd/dist/antd.css';
import { Select, Typography, Button } from 'antd';
import ReactEcharts from 'echarts-for-react';
const { Option } = Select;
const { Text } = Typography;

function getCookie(name) {
  if (!document.cookie) {
    return null;
  }

  const xsrfCookies = document.cookie.split(';')
    .map(c => c.trim())
    .filter(c => c.startsWith(name + '='));

  if (xsrfCookies.length === 0) {
    return null;
  }

  return decodeURIComponent(xsrfCookies[0].split('=')[1]);
}

const option = {
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  legend: {
    data: ['location1', 'location2']
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: [
    {
      type: 'value'
    }
  ],
  yAxis: [
    {
      type: 'category',
      axisTick: { show: false },
      data: []
    }
  ],
  series: [
    {
      name: 'location1',
      type: 'bar',
      label: { 
        show: true,
        fontWeight: "bold",
        padding: 0,
        position: 'right',
      },
      data: []
    },
    {
      name: 'location2',
      type: 'bar',
      label: {  
        show: true,
        fontWeight: "bold",
        padding:0,
        position: 'right',
      },
      data: []
    }
  ]
};



class ChartComponent extends React.Component {
  state = {
    echart: null,
    locations: [],
    years: [],
    types: [],
    location1:null,
    location2:null,
    year:null,
  };


  fetchOptions() {
    fetch('http://localhost:8000/api/getDistinctValue')
      .then(response => {
        if (response.status !== 200) {
          console.log("not success", response);
          return;
        } else {
          response.json().then(data => {
            if (data) {
              this.setState((state) => {
                return { ...state, years: data.yearRange, locations: data.location, types: data.type}
              })
              return
            }
          })
        }
      }).catch((e) => console.log(e))
  }
  fetchOptions2(chart) {
    fetch('http://localhost:8000/api/getDistinctValue')
      .then(response => {
        if (response.status !== 200) {
          console.log("not success", response);
          return;
        } else {
          response.json().then(data => {
            chart.setOption({
                ... option,
                yAxis: {
                  data: data.type
                }
            })
          })
        }
      }).catch((e) => console.log(e))
  }

  fetchResultData() {
    fetch('http://localhost:8000/api/getVaccinationForTwoLocation',
    {
      method: 'post',
      body: JSON.stringify({'location1': this.state.location1, 'location2': this.state.location2, 'year': this.state.year}),
    }).then(response => {
        if (response.status !== 200) {
          console.log("not success", response);
          return;
        } else {
          response.json().then(data => {
            console.log(this.state.location1, this.state.location2,'htz')
            if (data) {
              this.state.chart.setOption({
                ... option,
                yAxis: {
                  data: this.state.types
                },
                series: [
                  {
                    data: data.location1.map(x=>x.total_number)
                  },
                  {
                    data:  data.location2.map(x=>x.total_number)
                  }
                ]
              })
              return
            }
          })
        }
      }).catch((e) => console.log(e))
  }

  handleChangeYear(value){
    this.setState((state) =>{
      return {...state, year:value}
    })
  }

  handleChangeLocation1(value){
    this.setState( (state) =>{
      return {...state, location1:value}
    })
  }

  handleChangeLocation2(value){
    this.setState((state)=>{
      return {...state, location2:value}
    })
  }

  componentDidMount() {
    this.fetchOptions()
  }

  onChartReadyCallback(echart){
    this.setState((state)=>{
      this.fetchOptions2(echart)
      return {...state, chart: echart}
    })
  }

  render() {
    return (
      <div>
        <div style={{ 'marginButtom': 10, 'marginLeft': 'auto', 'marginRight': 'auto' }}>
          <span style={{ 'marginRight': 5 }}>
            <Text>Location1: </Text>
            <Select style={{ width: 200 }} onChange={(v) => this.handleChangeLocation1(v)}>
              {this.state.locations.map(value => {
                return <Option value={value}>{value}</Option>
              })}
            </Select>
          </span>
          <span style={{ 'marginLeft': 5 }}>
            <Text>Location2: </Text>
            <Select style={{ width: 200 }} onChange={(v)=>this.handleChangeLocation2(v)}>
              {this.state.locations.map(value => {
                if (value != this.state.select2) {
                  return <Option value={value}>{value}</Option>
                }
              })}
            </Select>
          </span>
          <span style={{ 'marginLeft': 5 }}>
            <Text>Year: </Text>
            <Select style={{ width: 200 }}  onChange={(v)=>this.handleChangeYear(v)}>
              {this.state.years.map(value => {
                return <Option value={value}>{value}</Option>
              })}
            </Select>
          </span>
          <span style={{ 'marginLeft': 5 }}>
            <Button type="primary" onClick={(e) => this.fetchResultData()} icon="search"> Search</Button>
          </span>
        </div>
        <div style={{ 'marginTop': 20 }}>
          <ReactEcharts option={option} onChartReady={(e) => this.onChartReadyCallback(e)}/>
        </div>
      </div>
    )
  }
}
export default ChartComponent;