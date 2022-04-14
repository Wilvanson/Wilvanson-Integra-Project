import { useEffect } from 'react';
import { BrowserRouter, Route, Switch} from 'react-router-dom';
import CrashPage from './components/404page';
import GraphPage from './components/Graphs';
import MedvCrimPage from './components/MedvCrim';
import MedvAgePage from './components/MedvAge';
import MedvPtratioPage from './components/MedvPtratio';

function App() {

  

  

  return (
    // <div>Hello World</div>
    <BrowserRouter>
      <Switch>
        <Route path='/' exact>
          <GraphPage />
        </Route>
        <Route path='/medvCrim'>
          <MedvCrimPage />
        </Route>
        <Route path='/medvAge'>
          <MedvAgePage />
        </Route>
        <Route path='/medvPtratio'>
          <MedvPtratioPage />
        </Route>
        <Route path='/'>
          <CrashPage />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
