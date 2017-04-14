import React from 'react'

export const Multiplier = (props) => (
  <div style={{ margin: '0 auto' }} >
    <h2>Multiplier: {props.counter}</h2>
    <button className='btn btn-default' onClick={props.increment}>
      Double
    </button>
    {' '}
    <button className='btn btn-default' onClick={props.doubleAsync}>
      Square (Async)
    </button>
  </div>
)

Multiplier.propTypes = {
  counter     : React.PropTypes.number.isRequired,
  doubleAsync : React.PropTypes.func.isRequired,
  increment   : React.PropTypes.func.isRequired
}

export default Multiplier
