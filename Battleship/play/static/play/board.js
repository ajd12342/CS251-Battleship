function Square(props) {
    return React.createElement(
        'button',
        {
            className: 'square',
            onClick: props.onClick },
        props.value
    );
}
class Board extends React.Component {
    constructor(props) {
        super(props);
        var x = new Array(10);

        for (var i = 0; i < x.length; i++) {
            x[i] = new Array(10);
        }

        this.state = {
            squares: x.fill(Array(10).fill(1))
        };
    }
    handleClick(i, j) {
        var squares = new Array(10);
        for (var k = 0; k < squares.length; k++) {
            squares[k] = this.state.squares[i].slice();
        }
        squares[i][j] = 2;
        this.setState({
            squares: squares
        });
    }
    renderSquare(i, j) {
        return React.createElement(Square, {
            value: this.state.squares[i][j],
            onClick: () => this.handleClick(i, j)
        });
    }
    render() {
        let rows = [];
        for (let i = 0; i < 10; i++) {
            for (let j = 0; j < 10; j++) {

                // note: we add a key prop here to allow react to uniquely identify each
                // element in this array. see: https://reactjs.org/docs/lists-and-keys.html
                rows.push(this.renderSquare(i, j));
            }
        }
        return React.createElement(
            'div',
            null,
            rows
        );
    }
}
ReactDOM.render(React.createElement(Board, null), document.getElementById('board_container'));