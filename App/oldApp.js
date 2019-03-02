import React from 'react';
import { ScrollView, StyleSheet, Text, View, Alert, Button} from 'react-native';
import {createStackNavigator, createAppContainer} from 'react-navigation';

import Header from './oldComponents/Header.js';
import Main from './oldComponents/Main.js';
import Footer from './oldComponents/Footer.js';

BASE_URL="http://192.168.43.42:5000"

export default class App extends React.Component {
  constructor(props){
    super(props);
    this.state = {};
    this.state.details = [];
    // this.getDetails();

    this.submit = this.submit.bind(this);
    this.pollDetails = this.pollDetails.bind(this);
    this.pollDetails();

    this.submit({
      "t_id": "1", 
      "ticket_data" : {
        "products_used": {
          "T-sensors": {
            "amount": 4,
          }
        },
        "is_resolved": 0, 
      }
    })    
  }

  async submit(data){
    // var d = this.format(data);
    try{
      var resp = await fetch(BASE_URL + "/update-ticket", {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      });
    }catch(error){

    }

  }

  format(data){
    return {t_id: data.t_id, new_data: data}
  }

  async pollDetails(t=2000){
    var last = await this.getDetails();
    setTimeout(this.pollDetails, t);
  }

  async getDetails(){
    try{
      let resp = await fetch(BASE_URL + "/unresolved-tickets");
      let response = await resp.json();

      var details = Object.keys(response).map(key =>{
        return {tokenId: key, ...response[key]}
      })
      // console.error(details)
      this.setState((state) => {
        return {...state, details}
      })
      return 1;
    }catch(error){
      console.error(error)
    }
    return 0;
  }


  render() {
    // this.state.details.forEach((ele) => {
    //   Alert.alert('New task!', ele.details)
    // })

    return (
      <ScrollView contentContainerStyle={styles.container}>
        <Header styles={styles.row}></Header>
        <Main details={this.state.details} styles={styles.row} buttonHandler={this.submit}></Main>
        {/*** <Footer styles={styles.row}></Footer> ***/}
      </ScrollView>
    );
  }
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    // alignItems: 'center',
    justifyContent: 'center',
  },
  row: {
    paddingLeft: 20,
    paddingRight: 20,
  }
});
