var counts=Array(5).fill(0);
function Square(props) {
    return React.createElement(
        'button',
        {
            onClick: props.onClick,
            className: 'square btn btn-square '+props.value,
        },
        '-'
    );
}
class Board extends React.Component {
    constructor(props) {
        super(props);
        var x = new Array(10);
        var y= new Array(10);
        for (var i = 0; i < x.length; i++) {
            x[i] = new Array(10);
            y[i]=new Array(10);
        }

        this.state = {
            squares: x.fill(Array(10).fill(0)),
            squareType: y.fill(Array(10).fill('')),
        };
    }
    handleClick(i, j) {
        let squares=jQuery.extend(true, {}, this.state.squares);
        squares[i][j] = 1;
        this.setState({
            squares: squares,
        });
    }
    renderSquare(i, j) {
        let k=10*i+j;
        let colour='btn-default';
        if(this.state.squares[i][j]===1){
            colour='btn-success';
        }
        return React.createElement(Square, {
            value: colour,
            onClick: () => this.handleClick(i, j),
            key: k,
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
            rows.push(React.createElement(
                'br',
                {
                    key: 'b'+i.toString(),
                },
            ));
        }
        rows.push(React.createElement(
            'h1',
            {
                key: 'choose',
            },
            'Choose ship type:'
        ));
        rows.push(React.createElement(
            "form",
            {
                key: 'ship-form',
            },
            React.createElement("input", { type: "radio", name: "ship", value: "1", defaultChecked: true }),
            "1*1",
            React.createElement("br", null),
            React.createElement("input", { type: "radio", name: "ship", value: "2" }),
            "2*1",
            React.createElement("br", null),
            React.createElement("input", { type: "radio", name: "ship", value: "3" }),
            "L-shaped",
            React.createElement("br", null),
            React.createElement("input", { type: "radio", name: "ship", value: "4" }),
            "4*1",
            React.createElement("br", null),
            React.createElement("input", { type: "radio", name: "ship", value: "5" }),
            "T-shaped",
        ));
    return React.createElement(
    'div',
    null,
    rows
);
}
}
ReactDOM.render(React.createElement(Board, null), document.getElementById('board_container'));