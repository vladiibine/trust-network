import React, { Component, PropTypes } from 'react'
import { browserHistory, Router } from 'react-router'
import { Provider } from 'react-redux'

import { App } from '../routes/TestApp'

class AppContainer extends Component {
  static propTypes = {
    routes : PropTypes.object.isRequired,
    store  : PropTypes.object.isRequired
  }

  shouldComponentUpdate () {
    return false
  }

  render () {
    const { routes, store } = this.props

    return (
        <div>
          <Provider store={store}>
            <div style={{ height: '100%' }}>
              <Router history={browserHistory} children={routes} />
            </div>
          </Provider>
          <App/>
        </div>
    )
  }
}

export default AppContainer
