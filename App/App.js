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
  }
  static navigationOptions = {
    title: 'Transformer Healthcare',
  };

  async pollDetails(t=10000){
    var last = await this.getDetails();
    setTimeout(this.pollDetails.bind(this), t);
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
    
    var items = this.state.details.length > 0 ? this.state.details.slice().map((ele, i) =>{
      var s = {...styles.card, ...styles.row, ...styles.cardOuter};
      
      if(this.state.newTickets[ele.tokenId]){
        
        s = {...s, ...styles.newTicket}
      }
      return (
        <TouchableHighlight onPress={() => this._onPressButton(i)} underlayColor="white" key={ele.tokenId}>
          <View style={s}>
            
            <Text style={styles.card} >{ele.details}</Text>
            <Text style={{...styles.card, ...styles.date}}>{ele.date}</Text>
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
        backgroundColor: '#005cb2',
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
    color: "#666",
    fontWeight: '600'
  },
  cardOuter:{
    borderWidth: 1,
    borderColor: '#eee',
    backgroundColor: '#fff',
  },
  card: {
    borderRadius: 6,
    color: "#222",
    fontSize: 14,
  },
  newTicket: {
    backgroundColor: '#f3cd3b'
  }
});
