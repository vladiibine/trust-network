//make a component, which has 1 radio box, and 1 input field for writing the temperature in celsius/fahrenheit
// A text field should write in red if the the water boils, at that temperature, or in green, if the water doesn't boil
import React from 'react'


function getCelsiusDegrees(value, scale){
  if(scale === 'celsius'){
    return value
  } else if (scale === 'fahrenheit'){
    // return (value - 32) * 9 / 5;
    return 5 / 9 * (value - 32);

  }
}

function getFahrenheitDegrees(value, scale){
  if (scale === 'celsius'){
    // return 5 / 9 * value + 32;
    return value * 9 / 5 + 32;
  } else if (scale === 'fahrenheit'){
    return value
  }
}


class ScaleRadio extends React.Component {
  constructor(props){
    super(props);
  }
  render(){
    return (
        <input type="radio" checked={this.props.checked} onChange={this.props.onChangeCallback}/>
    )
  }
}


class BoilingDeterminer extends React.Component{
  render(){
    const celsiusTemperature = getCelsiusDegrees(this.props.value, this.props.scale);
    return (
      <div>The water will {celsiusTemperature >= 100 ? '' : 'not '} boil.</div>
    )
  }
}

class InputField extends React.Component{
  render(){
    return (
        <input type="text" value={this.props.value} onChange={this.props.onChangeCallback}/>
    )
  }
}

export class App extends React.Component{
  constructor(props){
    super(props);
    this.state = this.createInitialState({celsiusChecked: true});

    this.handleChangedFahrenheit = this.handleChangedFahrenheit.bind(this);
    this.handleChangedCelsius = this.handleChangedCelsius.bind(this);
    this.handleInputChange = this.handleInputChange.bind(this);
  }

  createInitialState(additionalState={}){
    let state = {
      degrees: '',
      scale: 'celsius',
    };

    state = Object.assign(state, additionalState);

    return state;
  }

  handleChangedFahrenheit(event){
    const scale = 'fahrenheit';
    this.setState(
        prevState => ({scale: scale, degrees: getFahrenheitDegrees(prevState.degrees, prevState.scale)})
    );
  }

  handleChangedCelsius(event){
    const scale = 'celsius';
    this.setState(
        prevState => ({scale: scale, degrees: getCelsiusDegrees(prevState.degrees, prevState.scale)})
    );
  }

  handleInputChange(event){
    this.setState({degrees: event.target.value})
  }

  render(){
    return (
      <div>
          <form>
            <fieldset>
              <ScaleRadio onChangeCallback={this.handleChangedFahrenheit} checked={this.state.scale === 'fahrenheit'} />
              <label htmlFor="scale">Fahrenheit</label>

              <ScaleRadio onChangeCallback={this.handleChangedCelsius} checked={this.state.scale === 'celsius'} />
              <label htmlFor="scale">Celsius</label>

              <InputField value={this.state.degrees}  onChangeCallback={this.handleInputChange} />

              <BoilingDeterminer value={this.state.degrees} scale={this.state.scale} />
            </fieldset>
        </form>
      </div>
    )
  }
}
