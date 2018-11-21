var counts=Array(6).fill(0);
var upperCount=Array(6).fill(0);
upperCount[1]=3;
upperCount[2]=2;
upperCount[3]=1;
upperCount[4]=1;
upperCount[5]=1;
function Square(props) {
    return React.createElement(
        'button',
        {
            onClick: props.onClick,
            className: 'square btn btn_cust '+props.value,
        },
         null,
    );
}
class Board extends React.Component {
    constructor(props) {
        super(props);
        var x = new Array(10);
        var y= new Array(6);
        let z=new Array(6);
        for (var i = 0; i < x.length; i++) {
            x[i] = new Array(10);
        }
        for(let i=1;i<y.length;i++){
            y[i]=[];
            z[i]=[];
        }
        this.state = {
            squares: x.fill(Array(10).fill(0)),
            iOfSquaresOfType: y,
            jOfSquaresOfType: z,
        };
    }
    handleClick(j, i) {
        let squares=jQuery.extend(true, {}, this.state.squares);
        let iOfSquaresOfType=jQuery.extend(true, {}, this.state.iOfSquaresOfType);
        let jOfSquaresOfType=jQuery.extend(true, {}, this.state.jOfSquaresOfType);
        let c=$('input[name=ship]:checked');
        if(c.length> 0){
            let choice=c[0];
            let shape=choice.value;
            let orientation=parseInt($('input[name=orientation]').val(),10);
            let ret=true;
            let xToCheck=[];
            let yToCheck=[];
            xToCheck.push(i);
            yToCheck.push(j);
            if(shape==='1'){
            }else if(shape==='2'){
                xToCheck.push(i+(orientation-3)*(orientation%2-1));
                yToCheck.push(j+(orientation-2)*(orientation%2));
            }else if(shape==='3'){
                xToCheck.push(i);
                yToCheck.push(j- (((orientation===1)||(orientation===4))?1:0) + (((orientation===2)||(orientation===3))?1:0));
                xToCheck.push(i+(((orientation===1)||(orientation===2))?1:0) - (((orientation===3)||(orientation===4))?1:0));
                yToCheck.push(j);
            }else if(shape==='4'){
                if(orientation%2===1){
                    for(let k=1;k<=3;k++){
                        xToCheck.push(i);
                        yToCheck.push(j-(k)*(2-orientation));
                    }
                }
                if(orientation%2===0){
                    for(let k=1;k<=3;k++){
                        xToCheck.push(i+(k)*(3-orientation));
                        yToCheck.push(j);
                    }
                }
            }else if(shape==='5'){
                if(orientation%2===1){
                    xToCheck.push(i+1);
                    xToCheck.push(i-1);
                    yToCheck.push(j);
                    yToCheck.push(j);
                    for(let k=1;k<=2;k++){
                        xToCheck.push(i);
                        yToCheck.push(j-(k)*(2-orientation));
                    }
                }
                if(orientation%2===0){
                    xToCheck.push(i);
                    xToCheck.push(i);
                    yToCheck.push(j+1);
                    yToCheck.push(j-1);
                    for(let k=1;k<=2;k++){
                        xToCheck.push(i+(k)*(3-orientation));
                        yToCheck.push(j);
                    }
                }
            }
            for(let k=0;k<xToCheck.length;k++){
                if(xToCheck[k]>9 || xToCheck[k]<0 || yToCheck[k]>9 || yToCheck[k]<0
                    || squares[yToCheck[k]][xToCheck[k]]===1){
                    ret=false;
                }
            }
            if(ret&&counts[shape]<upperCount[shape]) {
                counts[shape]++;
                for(let k=0;k<xToCheck.length;k++){
                    squares[yToCheck[k]][xToCheck[k]]=1;
                    iOfSquaresOfType[shape].push(yToCheck[k]);
                    jOfSquaresOfType[shape].push(xToCheck[k]);
                }
                this.setState({
                    squares: squares,
                    iOfSquaresOfType: iOfSquaresOfType,
                    jOfSquaresOfType: jOfSquaresOfType,
                });
            }
        }
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
            React.createElement(
                'ul',
                {
                    id: 'ul',
                },
                React.createElement(
                    'li',
                    {
                        id: '1',
                    },
                    React.createElement("input", { type: "radio", name: "ship", id: 's1', value: "1", orientationv: "1", defaultChecked: true }),
                    React.createElement("label",{htmlFor: "s1"},'1*1'),
                ),
            React.createElement(
                    'li',
                    {
                        id: '2',
                    },
                    React.createElement("input", { type: "radio", name: "ship", id: 's2', value: "2", orientationv: "1"}),
                    React.createElement("label",{htmlFor: "s2"},'2*1'),
                ),
            React.createElement(
                    'li',
                    {
                        id: '3',
                    },
                    React.createElement("input", { type: "radio", name: "ship", id: 's3', value: "3", orientationv: "1"}),
                    React.createElement("label",{htmlFor: "s3"},'L-shaped'),
                ),
            React.createElement(
                    'li',
                    {
                        id: '4',
                    },
                    React.createElement("input", { type: "radio", name: "ship", id: 's4', value: "4", orientationv: "1"}),
                    React.createElement("label",{htmlFor: "s4"},'4*1'),
                ),
            React.createElement(
                    'li',
                    {
                        id: '5',
                    },
                    React.createElement("input", { type: "radio", name: "ship", id: 's5', value: "5", orientationv: "1"}),
                    React.createElement("label",{htmlFor: "s5"},'T-shaped'),
                )
            ),
        ));
        rows.push(React.createElement(
            'button',
            {
                key:'submit',
                id: 'submit',
                className: 'btn btn-success',
                onClick: this.submitClick(),
            },
            'Submit'
        ));
        return React.createElement(
            'div',
            null,
            rows
        );
    }
}
let b=React.createElement(Board,null);
ReactDOM.render(b, document.getElementById('board_container'));
