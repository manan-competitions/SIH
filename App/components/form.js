import React from 'react';
import { 
	TouchableHighlight, 
	Button, 
	View, 
	Text, 
	StyleSheet, 
	Picker, 
	TextInput, 
	CheckBox
} from 'react-native';

import { BASE_URL } from '../config.js';

export default class FormScreen extends React.Component {
  constructor(props){
  	super(props);
  	this.state = {};
  	this.state.formData = {};

  	const { navigation } = this.props;
  	this.state.formData.t_id = navigation.getParam('id', -1);
  	this.state.formData.ticket_data = {};   
  }
  static navigationOptions = (nav) =>{
    return {
    'title': 'Forms',
    }
  };

  setField(data, path){
    this.setState((state)=>{
      var formData = Object.assign({}, state.formData);
      var l = path.length;
      var curr = formData;
      for(var i = 0; i< l - 1; i++){
      	var name = path[i];
      	if(curr[name] == undefined){
      		curr[name] = {};
      	}
      	curr = curr[name];
      }
      curr[path[l - 1]] = data;
      return {...state, formData};
    })
  }

  async submit(data){
    try{
      var resp = await fetch(BASE_URL + "/update-ticket", {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      });
      this.props.navigation.navigate('Home');
    }catch(error){

    }

  }

  render(){

    var textFieldData = [  
    {
      "label": "Amount of T-sensors used",
      "placeholder": "0",
      
      "path": ["ticket_data", "products_used", "T-sensors", "amount"],
    }, 
    {
      "label": "Amount of Wires used",
      "placeholder": "0",
      
      "path": ["ticket_data", "products_used", "Wires", "amount"],
    }, 
    {
      "label": "Feedback",
      "placeholder": "",
      "path": ["ticket_data", "feedback"],
    }]

    var textFields = textFieldData.map((ele, i) =>{
      return (<View style={styles.field} key={i}>
            <Text>{ele.label}</Text>
            <TextInput placeholder={ele.placeholder} style={styles.input}
              onChangeText={(text) => this.setField(text, ele.path)}
            ></TextInput>
          </View>)
    })

    // var selectFieldsData = [{
    //   "label": "pick field",
    //   "options": [
    //   {
    //     "label": "one",
    //     "value": "one",
    //   }, 
    //   {
    //     "label": "two",
    //     "value": "two",
    //   },
    //   {
    //     "label": "three",
    //     "value": "three",
    //   }
    //   ],
    //   name: "picker"
    // }]

    // var selectFields = selectFieldsData.map((ele, i) =>{
    //   var options = ele.options.map((e, ind) => 
    //     <Picker.Item label={e.label} value={e.value} key={ind}/>)
    //   return (<View style={styles.field} key={i}>
    //         <Text>{ele.label}</Text>
    //         <Picker
    //           selectedValue={this.state.formData[ele.name] || ele.options[0]["value"]}
    //           onValueChange={(val) =>
    //             this.setField(val, ele.name)
    //           }>
    //           {options}
    //         </Picker>
    //       </View>)
    // })

    // {selectFields}
    return (<View style={{justifyContent: 'space-between', flex: 1, padding: 20}}>
    		<View style={styles.form}>
              {textFields}
              
              <View style={styles.flexRow}>
                <CheckBox value={this.state.formData["ticket_data"]["is_resolved"] || false} 
                onValueChange={(val) => this.setField(val, ["ticket_data", "is_resolved"])} ></CheckBox>
                <Text>Resolved</Text>
              </View>
              
            </View>
            <TouchableHighlight onPress={() => this.submit(this.state.formData)} 
           underlayColor="white" >
         		<View style={styles.submitButton}><Text style={styles.submitButton}>Submit</Text></View>
         	</TouchableHighlight>
            </View>)
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
  },
  pageStyle:{
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
  }, 
  submitButton: {
  	alignSelf: 'flex-end',
  	borderRadius: 6,
  	backgroundColor: '#a1e978',
  	padding: 10, 
  	fontWeight: 'bold'
  }
});
