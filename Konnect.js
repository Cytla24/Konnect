import React from 'react';
import "@blueprintjs/core";
import "@blueprintjs/core/lib/css/blueprint.css"
import "@blueprintjs/icons/lib/css/blueprint-icons.css"
import BackgroundSlideshow from 'react-background-slideshow'
import { Button, Card, Elevation } from "@blueprintjs/core";
import StarRatings from 'react-star-ratings';
import background1 from './images/background1.jpg'
import background2 from './images/background2.jpg'
import MyCard from './MyCard.js'


// import {
// 	BrowserRouter as Router,
// 	Switch,
// 	Route,
// 	Link
// } from 'react-router-dom';
import {Link} from 'react-router-dom'
import './Konnect.css'

class Konnect extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			searchVal:"a",
			data:[
			],
			filteredData: []
		}
		this.search = this.search.bind(this);
		this.onChange = this.onChange.bind(this);
		this.cards = this.cards.bind(this);
	  }

	componentDidMount(){
		fetch('/allBusiness')
		.then(results => {
			return results.json();
		}).then(
			results=>results.sort((a, b) => b.rating-a.rating)
		)
		.then(results=>{
			console.log(results)
			this.setState({filteredData: results})
			this.setState({data: results})
		})
	}
	

	cards(){
		return this.state.filteredData.map((x)=>
			<div className="cards">
				<MyCard x={x}/>
			</div>
		)
	}
	

	search(){
		console.log(this.state.searchVal);
		var data = this.state.data.filter(val=> {return val.name.indexOf(this.state.searchVal) !== -1} )
		this.setState({filteredData:data})
	}

	onChange(e){
		this.setState({searchVal:e.target.value})
		console.log(e.target.value)
	}


	render(){
		fetch('/addTweets')
		return (
            <div className = "background">
				{/* <BackgroundSlideshow images={[background1, background2]}/> */}
                {/* <div className = 'App-header'>Konnect</div> */}
				<nav className="bp3-navbar bp3-dark">
					<div className="bp3-navbar-group bp3-align-left">
						<div className="bp3-navbar-heading"><h1>KONNECT</h1></div>
						{/* <input className="bp3-input" placeholder="Search songs..." type="text" /> */}
					</div>
					<div className="bp3-navbar-group bp3-align-right">
						<Link className="bp3-button bp3-minimal bp3-icon-contacts" to="/Konnect">Contact</Link>
						<span className="bp3-navbar-divider"></span>
						<button className="bp3-button bp3-minimal bp3-icon-user"></button>
						<button className="bp3-button bp3-minimal bp3-icon-cog"></button>
					</div>
				</nav>
				
				<div >
					<div className = "SearchBar">
						<div className="bp3-input-group bp3-round bp3-large bp3-intent-primary bp3-fill .modifier">
							{/* <form onSubmit={this.search}> */}
								<span className="bp3-icon bp3-icon-search"></span>
									<input type="text" className="bp3-input" placeholder="Search Konnect..." onChange = {this.onChange}/>
								<button className="bp3-button bp3-minimal bp3-intent-primary bp3-icon-arrow-right" onClick = {this.search}></button>
							{/* </form> */}
						</div>
					</div>
				</div>
				
				<div>{this.cards()}</div>
				      
				
            </div>		
		)
	}
	
	
}

export default Konnect;

/*
	componentDidMount(){
		console.log("Hey what's up b")
		const url="/books"
		fetch(url)
			.then((data)=>data.json())
			.then((data)=>{this.setState({books:data})})
	}
*/