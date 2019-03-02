import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export default class Header extends React.Component {
  render() {
    return (	
    	<View style={{...styles.container, ...this.props.styles}}>
	      <Text style={styles.typography}>Transformer Healthcare</Text>
	    </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
  	paddingTop: 50,
  	paddingBottom: 10,
    backgroundColor: '#005cb2',
    // alignItems: 'center',
    justifyContent: 'center',
  },
  typography:{
  	fontSize: 22,
  	fontWeight: "300",
  	color: '#fff',
  }
});