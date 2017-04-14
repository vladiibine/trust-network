import { injectReducer } from '../../store/reducers'

export default (store) => {
  debugger;
  return {
  path : 'multiplier',
  /*  Async getComponent is only invoked when route matches   */
  getComponent (nextState, cb) {
    /*  Webpack - use 'require.ensure' to create a split point
        and embed an async module loader (jsonp) when bundling   */
    require.ensure([], (require) => {
      /*  Webpack - use require callback to define
          dependencies for bundling   */
      const Multiplier = require('./containers/MultiplierContainer').default
      const reducer = require('./modules/multiplier').default

      /*  Add the reducer to the store on key 'multiplier'  */
      injectReducer(store, { key: 'multiplier', reducer })

      /*  Return getComponent   */
      cb(null, Multiplier);

    /* Webpack named bundle   */
    }, 'multiplier')
  }
}
}