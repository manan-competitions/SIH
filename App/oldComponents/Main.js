import React from 'react';
import { 
  Picker, 
  Button, 
  SectionList, 
  ViewPagerAndroid, 
  ScrollView, 
  TextInput, 
  StyleSheet, 
  Text, 
  View,
  CheckBox
} from 'react-native';

export default class Main extends React.Component {
  constructor(props){
    super(props);
    this.state = {}
    this.state.formData = {}
    this.state.tab = 0;
    this.changeTab = this.changeTab.bind(this);
  }

  setField(data, name){
    this.setState((state)=>{
      var formData = Object.assign({}, state.formData);
      formData[name] = data;
      return {state, formData};
    })
  }
  
  changeTab({nativeEvent}){
    
    this.setState((state) => {
      return {...state, tab: nativeEvent.position};
    })
  }
  

  render() {
  	var items = this.props.details.map((ele, i) =>{
  		return (<View key={ele.tokenId} style={styles.pane}>
        <Text style={styles.text}>TokenId : {ele.tokenId}</Text>
  			<Text style={styles.text}>Details : {ele.details}</Text>
        <Text style={styles.text}>Date : {ele.date}</Text>
  			</View>)
  	})
    
    var textFieldData = [{
      "label": "Token ID",
      "placeholder": "123",
      "name": "t_id",
    }, {
      "label": "What went wrong?",
      "placeholder": "Oh! It's just a bug inside.",
      "name": "bug",
    },  {
      "label": "One more field",
      "placeholder": "one more answer",
      "name": "one",
    }]

    var textFields = textFieldData.map((ele, i) =>{
      return (<View style={styles.field} key={i}>
            <Text>{ele.label}</Text>
            <TextInput placeholder={ele.placeholder} style={styles.input}
              onChangeText={(text) => this.setField(text, ele.name)}
            ></TextInput>
          </View>)
    })

    var selectFieldsData = [{
      "label": "pick field",
      "options": [
      {
        "label": "one",
        "value": "one",
      }, 
      {
        "label": "two",
        "value": "two",
      },
      {
        "label": "three",
        "value": "three",
      }
      ],
      name: "picker"
    }]

    var selectFields = selectFieldsData.map((ele, i) =>{
      var options = ele.options.map((e, ind) => 
        <Picker.Item label={e.label} value={e.value} key={ind}/>)
      return (<View style={styles.field} key={i}>
            <Text>{ele.label}</Text>
            <Picker
              selectedValue={this.state.formData[ele.name] || ele.options[0]["value"]}
              onValueChange={(val) =>
                this.setField(val, ele.name)
              }>
              {options}
            </Picker>
          </View>)
    })

// <View style={styles.tabCont}>
//         <View style={{...styles.tab, ...(this.state.tab == 0 ? styles.selected : {})}}>
//           <Text style={styles.ctext}>Form</Text>
//         </View>
//         <View style={{...styles.tab, ...(this.state.tab == 1 ? styles.selected : {})}}>
//           <Text style={styles.ctext}>List</Text>
//         </View>
//       </View>

    return ( this.props.details.length > 0 ? (
      <ScrollView contentContainerStyle={styles.content}>        
        <ViewPagerAndroid style={styles.content}
          onPageSelected={this.changeTab}>
          <View style={{...styles.pageStyle,  ...this.props.styles}} key="1">
            <View style={styles.form}>
              {textFields}
              {selectFields}
              <View style={styles.flexRow}>
                <CheckBox value={this.state.formData["is_resolved"] || false} 
                onValueChange={(val) => this.setField(val, "is_resolved")} ></CheckBox>
                <Text>Resolved</Text>
              </View>
              <View>
                <Button style={styles.pretty_button} color="#2196f3" title="Submit" 
                onPress={() =>this.props.buttonHandler(this.state.formData)}></Button>
              </View>
            </View>
          </View>
          <View style={{...styles.pageStyle,...this.props.styles}} key="2">
            <ScrollView>
              {items}
            </ScrollView>
          </View>
        </ViewPagerAndroid>
      </ScrollView>      
      ) : (<View style={{backgroundColor: "#ddd",flex: 5, color: "#fff", display: 'flex', justifyContent:"center", alignItems: "center"}}>
      <Text style={{fontWeight: "500"}}> Everything is working fine.</Text>
      </View>)
    );
  }
}

const styles = StyleSheet.create({
  pane: {
    margin: 10,
    backgroundColor: '#1e88e5',
    padding: 10,
    borderRadius: 6,
  },
  text:{
    color: '#fff',
    fontSize: 16,
    fontWeight: "500",
  },
  form:{
  	borderColor: '#eee',
    backgroundColor: '#fff',
  	borderWidth: 1,
  	margin: 20,
  	padding: 10,
  },
  input:{
  	borderBottomWidth: 1,
  	borderBottomColor: '#eee',
    marginBottom: 10,
  },
  field:{
  	marginBottom: 20,
  },
  content: {
    flex: 5,
    display: 'flex',
    justifyContent: 'center',
    // backgroundColor: '#fff',
    // borderColor: '#000000',
    // borderWidth: 2,
  },
  pageStyle:{
    // paddingTop: 10,
    backgroundColor: "#eee",
  },
  token: {
    
  },
  pretty_button: {
    borderRadius: 6,
    margin: 10,
    backgroundColor: "#000",
  }, 
  tab: {
    flex: 1,
    textAlign: 'center',
    color: "#fff",
    padding: 5,
    backgroundColor: '#005cb2'
  },
  selected: {
    backgroundColor: '#2195f2',
    color: '#000'
  },
  tabCont: {
    display: 'flex',
    flexDirection: 'row'
  },
  ctext: {
    textAlign: 'center', 
    color: "#fff"
  },
  flexRow: {
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'center'
  }
});
