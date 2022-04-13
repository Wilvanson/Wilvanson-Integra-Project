import { useEffect } from 'react';
import { BrowserRouter, Route, Switch} from 'react-router-dom';
import CrashPage from './components/404page';
import GraphPage from './components/Graphs';

function App() {

  

  

  return (
    // <div>Hello World</div>
    <BrowserRouter>
      <Switch>
        <Route path='/' exact>
          <GraphPage />
        </Route>
        <Route path='/'>
          <CrashPage />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
