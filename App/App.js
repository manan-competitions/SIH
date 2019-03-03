import React from 'react';
import { TouchableHighlight, Button, View, Text, StyleSheet, Vibration } from 'react-native';
import { createStackNavigator, createAppContainer } from 'react-navigation'; // Version can be specified in package.json

import FormScreen from './components/form.js';
import DetailsScreen from './components/details.js';

import { BASE_URL } from './config.js';

class HomeScreen extends React.Component {
  constructor(props){
    super(props)
    this.state = {};
    this.state.details = [];
    this.state.newTickets = {};
    this._onPressButton = this._onPressButton.bind(this);
    this.getDetails = this.getDetails.bind(this);
    this.pollDetails.bind(this)();
    // this.state.newTickets = {"2": true, "1": false}
    // this.state.details = [
    // {
    //     "tokenId": "2",
    //     "transformer_id": "1",
    //     "date": 1551564300.090039,
    //     "is_resolved": false,
    //     "is_new": false,
    //     "details": "oil_pump sensor has generated a critical alert again",
    //     "feedback": "Fghvh",
    //     "products_used": {
    //         "T-sensors": {
    //             "amount": "1"
    //         },
    //         "Wires": {
    //             "amount": "1"
    //         }
    //     }
    // },
    // {
    //     "tokenId":"1",
    //     "transformer_id": "1",
    //     "date": 1551564300.090039,
    //     "is_resolved": false,
    //     "is_new": true,
    //     "details": "oil_pump sensor has generated a critical alert",
    //     "feedback": "Fghvh",
    //     "products_used": {
    //         "T-sensors": {
    //             "amount": "1"
    //         },
    //         "Wires": {
    //             "amount": "1"
    //         }
    //     }
    // }]
  }
  static navigationOptions = {
    title: 'E Technician',
  };

  async pollDetails(t=800){
    var last = await this.getDetails();
    setTimeout(this.pollDetails.bind(this), t);
  }

  formatDate(date){
    return (new Date(date*1000)).toLocaleDateString();
  }

  async getDetails(){
    try{
      let resp = await fetch(BASE_URL + "/unresolved-tickets");
      let response = await resp.json();

      var details = Object.keys(response).map(key =>{
        return {tokenId: key, ...response[key]}
      })

      var newTickets = {};
      Object.keys(response)
        .forEach(ele => {
          newTickets[ele] = eval(response[ele].is_new) || this.state.newTickets[ele] || false
        })

      if(Object.keys(newTickets).filter(ele => newTickets[ele]).length > 0){
        Vibration.vibrate(1000)
      }
      
      this.setState((state) => {
        return {...state, details, newTickets}
      })

      return 1;
    }catch(error){
      console.error(error)
    }
    return 0;
  }

  _onPressButton(id){
    var {push} = this.props.navigation;
    var newTickets = this.state.newTickets;
    newTickets[this.state.details[id].tokenId] = false;
    this.setState((state)=>{
      return {...state, ...newTickets}
    });
    push('Details', {details: this.state.details[id]});
  }

  render() {    
    
    var items = this.state.details.length > 0 ? this.state.details.slice().reverse().map((ele, i) =>{
      var s = {...styles.card, ...styles.row, ...styles.cardOuter};
      var p = this.state.newTickets[ele.tokenId]? styles.newTicket: {};
      return (
        <TouchableHighlight onPress={() => this._onPressButton(i)} underlayColor="white" key={ele.tokenId}>
          <View style={{...s, ...p}}>
            
            <Text style={{...styles.card, ...p}} >{ele.details}</Text>
            <Text style={{...styles.card, ...styles.date, ...p}}>{this.formatDate(ele.date)}</Text>
          </View>
        </TouchableHighlight>)
    }) : (<Text style={{padding: 20, justifyContent: 'center'}}> All fixed for now </Text>)
        
    return (
      <View style={styles.container}>
        {items}
      </View>
    );
  }
}

const RootStack = createStackNavigator(
  {
    Home: HomeScreen,
    Details: DetailsScreen,
    Form: FormScreen,
  },
  {
    defaultNavigationOptions: {
      headerStyle: {
        
        backgroundColor: '#6b5aed',
        
      },
      headerTintColor: '#fff',
      headerTitleStyle: {
        fontWeight: 'bold',
      },
    }
  }
);

const AppContainer = createAppContainer(RootStack);

export default class App extends React.Component {
  render() {
    return <AppContainer />;
  }
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    // alignItems: 'center',
    // justifyContent: 'center',
  },
  row: {
    marginLeft: 20,
    marginRight: 20,
    marginTop: 20,
    padding: 10,
  },
  date: {
    textAlign: 'right', 
    fontSize: 11,
    color: "#222",
    fontWeight: '600'
  },
  cardOuter:{
    borderWidth: 1,
    borderColor: '#eee',
    backgroundColor: '#fff',
  },
  card: {
    borderRadius: 6,
    color: "#0a022f",
    fontSize: 14,
  },
  newTicket: {
    backgroundColor: '#9fa8da',
    color: "#fff"
  }
});
