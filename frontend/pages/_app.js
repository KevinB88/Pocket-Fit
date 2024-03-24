import '../styles/styles.css';
import { Component } from 'react';

class MyApp extends Component {
  render() {
    const { Component, pageProps } = this.props;

    return <Component {...pageProps} />;
  }
}

export default MyApp;