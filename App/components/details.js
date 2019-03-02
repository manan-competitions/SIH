import React from 'react';
import { TouchableHighlight, Button, View, Text, StyleSheet } from 'react-native';

export default class DetailsScreen extends React.Component {
  static navigationOptions = (nav) =>{
    return {
    'title': 'Details',
    }
  };

  formatDate(date){
    return (new Date(date*1000)).toLocaleDateString();
  }

  render() {
    const { navigation } = this.props;
    const details = navigation.getParam('details', null);
    if(!details){
      return (<View>Try Reloading the app</View>)
    }
    
    return (
      <View style={{...styles.details, ...styles.detailsOuter}}>
        <View>
          <Text style={{...styles.details, ...styles.tag}}>#{details.tokenId}</Text>
          <View style={styles.text}>
            <Text style={styles.details}>Problem detail: {details.details}</Text>
            <Text style={styles.details}>Previous Feedback: {details.feedback}</Text>
            <Text style={styles.details}>Transformer Id: {details.transformer_id}</Text>
            <Text style={styles.details}>Date: {this.formatDate(details.date)}</Text>
          </View>
        </View>
        <TouchableHighlight onPress={() => this.props.navigation.navigate('Form', {id: details.tokenId})} 
           underlayColor="white" >
         <View style={styles.prettyButton}>
           <View style={styles.prettyLine}></View>
           <View style={styles.prettyLine}></View>
           <View style={styles.prettyLine}></View>
         </View>
        </TouchableHighlight>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  detailsOuter: {
    flex: 1,
    padding: 20
  },
  details: {
    // backgroundColor: "#fff",
    color: "#222",
    justifyContent: 'space-between',

  },
  prettyButton: {
    backgroundColor: "#e94848",
    color: "#fff",
    borderRadius: 25,
    padding: 10,
    width: 50,
    height: 50,
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    alignSelf: 'flex-end'
  },
  prettyLine: {
    height: 0,
    width: 30,
    margin: 2,
    borderWidth: 1,
    borderBottomColor: '#fff',
    borderTopColor: '#fff',
    borderLeftColor: '#fff',
    borderRightColor: '#fff',
  },
  tag: {
    fontWeight: 'bold',
  },
  text: {
    // borderWidth: 2,
    // borderColor: '#eee',
    padding: 10,
    marginTop: 10,
    backgroundColor: "#eee",
  }
});