import React from "react";
import { render } from "react-dom";
import { withStyles } from 'material-ui';
import { Paper, Tabs, Tab } from 'material-ui';

const styles = {
  root: {
    flexGrow: 1,
  },
};

export default props => (
  <Paper>
    <Tabs
      value={0}
      indicatorColor="primary"
      textColor="primary"
      centered
    >
      <Tab label="Item One" />
      <Tab label="Item Two" />
      <Tab label="Item Three" />
    </Tabs>
  </Paper>
);