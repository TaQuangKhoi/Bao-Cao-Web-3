console.log("Khôi nhớ Hảo")

function Hello(props) {
    return <>

    </>;
}

class Container extends React.Component {
    render() {
        return <div ref={ ref => ref.appendChild(this.props.child) }></div>;
    }
}

const container = document.getElementById("rank-input");
const selectRanks = document.getElementById("select-ranks");
// remove selectRanks on DOM
// selectRanks.remove();

const root = ReactDOM.createRoot(container);
// root.render(<Container child={ selectRanks }/>);