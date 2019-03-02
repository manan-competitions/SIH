import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export default class Footer extends React.Component {
  render() {
    return (
      <Text style={{...styles.container, ...this.props.styles}}>
      Report complaints at +91 1111999922229
      </Text>
    );
  }
}

const styles = StyleSheet.create({
  container: {
  	flex: 1,
    backgroundColor: '#009688',
    alignItems: 'center',
    justifyContent: 'center',
  },
});