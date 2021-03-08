import React from 'react';
import logo from './logo.svg';
import './App.css';
import TableComponent from './table/table.js'
// import IconLinkComponent from './icon/icon.js'
import ChartComponent from './chart/chart.js'
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import { Row, Col, Layout, Icon, Button } from 'antd';
const { Header, Footer, Content } = Layout;


function App() {
  function iconOnClickHandler(){
    window.location = '/'
  }

  return (
    <Router>
      <div className="App">
        <Layout style={{ 'height': '100vh' }}>
          <Header style={{ 'backgroundColor': 'black' }}>
             <Icon onClick={(e) => iconOnClickHandler()} style={{color: 'white', fontSize: '3rem'}} type="area-chart" />
          </Header>
          <Content style={{ 'backgroundColor': 'white' }}>
            <Route exact path="/detail" component={detail} />
            <Route exact path="/" component={home} />
          </Content>
          <Footer style={{ 'height': '1rem' }}><div style={{ 'margin': '-0.5rem auto' }}>©2019 CMPUT401 Team callback Cats</div></Footer>
        </Layout>

      </div>
    </Router>
  );
}

function home() {
  return (
    <div style={{ 'marginTop': '25vh' }}>
      <Row>
        <Col span={4}></Col>
        <Col span={16}>
          <Row type="flex" justify="space-around" align="bottom">
              <ChartComponent></ChartComponent>
          </Row>
          {/* <Row style={{marginTop: 10}} type="flex" justify="space-around" align="bottom">
              <IconLinkComponent></IconLinkComponent>
          </Row> */}
        </Col>
        <Col span={4}></Col>
      </Row>
    </div>
  )
}


function detail() {
  return (
    <>
      <Row>
        <Col span={4}></Col>
        <Col span={16}>
          <TableComponent></TableComponent>
        </Col>
        <Col span={4}></Col>
      </Row>
    </>

  )
}

export default App;
