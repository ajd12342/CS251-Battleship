

'use strict';


class Board extends React.Component {
  constructor(props) {
    super(props);

  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Like'
    );
  }
}
const domContainer = document.querySelector('#board_container');
$(document).ready(function () {
    ReactDOM.render(e(Board), domContainer);
});