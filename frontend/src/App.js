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


const currencies = [
  {
    value: 'USD',
    label: '$',
  },
  {
    value: 'EUR',
    label: '€',
  },
  {
    value: 'BTC',
    label: '฿',
  },
  {
    value: 'JPY',
    label: '¥',
  },
];

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

export default function OutlinedTextFields() {
  const classes = useStyles();
  var [values, setValues] = React.useState({
  });

  const [state, setState] = React.useState({
    isDirected: false,
    isMultigraph: false,
    hasSelfLoops: false,
    weights: false,
  });

  const { isDirected, isMultigraph, hasSelfLoops, weights} = state;

  const handleChange = name => event => {
    setValues({ ...values, [name]: event.target.value });
    setState({ ...state, [name]: event.target.checked });
    console.log('hello')
    console.log(values.weights)
  };


  return (
    
    <form className={classes.container} noValidate autoComplete="off">
      <TextField
        id="numOfNodes"
        label="Number of Nodes"
        value={values.numOfNodes}
        onChange={handleChange('age')}
        type="number"
        className={classes.textField}
        margin="normal"
        variant="outlined"
      />
      <Divider variant="middle" component='form'/>

      <TextField
        id="numOfEdges"
        label="Number of Edges"
        value={values.numOfEdges}
        onChange={handleChange('age')}
        type="number"
        className={classes.textField}
        margin="normal"
        variant="outlined"
      />

      <Divider variant="middle" />

      <FormControl component="fieldset" className={classes.formControl}>
        <FormLabel component="legend"></FormLabel>
        <FormGroup>
          <FormControlLabel
            control={<Checkbox checked={isDirected} onChange={handleChange('isDirected')} value={values.isDirected} />}
            label="is directed"
          />
          <FormControlLabel
            control={<Checkbox checked={isMultigraph} onChange={handleChange('isMultigraph')} value={values.isMultigraph}/>}
            label="is multigraph"
          />
          <FormControlLabel
            control={
              <Checkbox checked={hasSelfLoops} onChange={handleChange('hasSelfLoops')} value={values.hasSelfLoops}/>
            }
            label="has self loops"
          />
        </FormGroup>
        <FormHelperText></FormHelperText>
      </FormControl>

      <FormControl component="fieldset" className={classes.formControl}>
        <FormLabel component="legend"></FormLabel>
        <FormGroup>
          <FormControlLabel
            id='weights'
            control={<Checkbox checked={weights} onChange={handleChange('weights')} value={values.weights} />}
            label="has weights"
          />
          <TextField
            disabled
            id="minWeight"
            label="minWeight"
            value={values.minWeight}
            onChange={handleChange('minWeight')}
            type="number"
            className={classes.textField}
            margin="normal"
            variant="outlined"
          />
          <TextField
            disabled={values.weights}
            id="maxWeight"
            label="maxWeight"
            value={values.maxWeight}
            onChange={handleChange('maxWeight')}
            type="number"
            className={classes.textField}
            margin="normal"
            variant="outlined"
          />

        <Typography component="div">
        <Grid component="label" container alignItems="center" spacing={1}>
          <Grid item>Integers</Grid>
          <Grid item>
            <Switch
              disabled
              checked={state.checkedC}
              onChange={handleChange('checkedC')}
              value={values.isFloat}
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
}
