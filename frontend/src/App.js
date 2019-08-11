import React from 'react';
import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import MenuItem from '@material-ui/core/MenuItem';
import TextField from '@material-ui/core/TextField';


import FormLabel from '@material-ui/core/FormLabel';
import FormControl from '@material-ui/core/FormControl';
import FormGroup from '@material-ui/core/FormGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import FormHelperText from '@material-ui/core/FormHelperText';
import Checkbox from '@material-ui/core/Checkbox';
import Divider from '@material-ui/core/Divider';
import Switch from '@material-ui/core/Switch';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles(theme => ({
  container: {
    display: 'flex',
    flexWrap: 'wrap',
    width: 'auto',
    marginLeft: theme.spacing(10),
    marginRight: theme.spacing(10),
    maxWidth: 1000,
    justify: 'center',
  },
  // textField: {
  //   marginLeft: theme.spacing(1),
  //   marginRight: theme.spacing(1),
  // },
  dense: {
    marginTop: theme.spacing(2),
  },
  menu: {
    width: 200,
  },
}));

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      numOfNodes: undefined,
      numOfEdges: undefined,
      isDirected: false,
      isMultigraph: false,
      hasSelfLoops: false,
      hasWeights: false,
      minWeight: undefined,
      maxWeight: undefined,
      isFloat: false,
    };

    this.handleChange = this.handleChange.bind(this);
    // this.handleSubmit = this.handleSubmit.bind(this);
    this.classes = this.classes.bind(this);
  }

  classes = useStyles;

  handleChange = name => event => {
    console.log(event.target.value)
    this.setState({ ...this.state, [name]: event.target.checked });
  };

  render() {
    return (
      <form className={this.classes.container} noValidate autoComplete="off">
        <TextField
          id="numOfNodes"
          label="Number of Nodes"
          value={this.state.numOfNodes}
          onChange={this.handleChange('numOfNodes')}
          type="number"
          className={this.classes.textField}
          margin="normal"
          variant="outlined"
        />

        <Divider variant="middle" component='form'/>

        <TextField
          id="numOfEdges"
          label="Number of Edges"
          value={this.state.numOfEdges}
          onChange={this.handleChange('numOfEdges')}
          type="number"
          className={this.classes.textField}
          margin="normal"
          variant="outlined"
        />

        <Divider variant="middle" />

        <FormControl component="fieldset" className={this.classes.formControl}>
          <FormLabel component="legend"></FormLabel>
          <FormGroup>
            <FormControlLabel
              control={<Checkbox checked={this.state.isDirected} onChange={this.handleChange('isDirected')} value={this.state.isDirected} />}
              label="is directed"
            />
            <FormControlLabel
              control={<Checkbox checked={this.state.isMultigraph} onChange={this.handleChange('isMultigraph')} value={this.state.isMultigraph}/>}
              label="is multigraph"
            />
            <FormControlLabel
              control={
                <Checkbox checked={this.state.hasSelfLoops} onChange={this.handleChange('hasSelfLoops')} value={this.state.hasSelfLoops}/>
              }
              label="has self loops"
            />
          </FormGroup>
          <FormHelperText></FormHelperText>
        </FormControl>

        <FormControl component="fieldset" className={this.classes.formControl}>
          <FormLabel component="legend"></FormLabel>
          <FormGroup>
            <FormControlLabel
              id='weights'
              control={<Checkbox checked={this.state.hasWeights} onChange={this.handleChange('hasWeights')} value={this.state.hasWeights} />}
              label="has weights"
            />
            <TextField
              disabled={this.state.hasWeights}
              id="minWeight"
              label="minWeight"
              value={this.state.minWeight}
              onChange={this.handleChange('minWeight')}
              type="number"
              className={this.classes.textField}
              margin="normal"
              variant="outlined"
            />
            <TextField
              disabled={this.state.hasWeights}
              id="maxWeight"
              label="maxWeight"
              value={this.state.maxWeight}
              onChange={this.handleChange('maxWeight')}
              type="number"
              className={this.classes.textField}
              margin="normal"
              variant="outlined"
            />

          <Typography component="div">
          <Grid component="label" container alignItems="center" spacing={1}>
            <Grid item>Integers</Grid>
            <Grid item>
              <Switch
                disabled={this.state.hasWeights}
                checked={this.state.isFloat}
                onChange={this.handleChange('isFloat')}
                value={this.state.isFloat}
              />
            </Grid>
            <Grid item>Decimal</Grid>
          </Grid>
        </Typography>

          </FormGroup>
          <FormHelperText></FormHelperText>
        </FormControl>
      </form>
    );
  };
}

export default App;