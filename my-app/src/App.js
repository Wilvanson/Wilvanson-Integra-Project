import { BrowserRouter, Route, Switch } from 'react-router-dom';
import CrashPage from './components/404page';

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path='/'>
          <CrashPage />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
