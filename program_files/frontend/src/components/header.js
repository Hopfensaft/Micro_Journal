import React from "react";
import { render } from "react-dom";
import PropTypes from "prop-types";
import { AppBar, Toolbar, Typography } from "material-ui";

const styles = {
  root: {
    flexGrow: 1
  },
  flex: {
    flex: 1
  },
  menuButton: {
    marginLeft: -12,
    marginRight: 20
  }
};

export default props => (
  <AppBar position="static">
    <Toolbar>
      <Typography variant="headline" color="inherit">
        Micro Journal
      </Typography>
    </Toolbar>
  </AppBar>
);