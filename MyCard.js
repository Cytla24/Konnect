import React from 'react';
import "@blueprintjs/core";
import "@blueprintjs/core/lib/css/blueprint.css"
import "@blueprintjs/icons/lib/css/blueprint-icons.css"

import { Button, Card, Elevation } from "@blueprintjs/core";
import StarRatings from 'react-star-ratings';
import './Konnect.css'


// import {
// 	BrowserRouter as Router,
// 	Switch,
// 	Route,
// 	Link
// } from 'react-router-dom';
import {Link} from 'react-router-dom'
import './Konnect.css'

class MyCard extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
            showMore : false,
        }
        this.toggle = this.toggle.bind(this)
      }
      
    toggle(){
        if (this.state.showMore){
            this.setState({showMore:false})
        }else{
            this.setState({showMore: true})
        }
    }

	render(){
		return (
            <Card interactive={true} elevation={Elevation.TWO}>
                
                <div className="bp3-icon-share name-header"><h3><a href={'https://www.google.com'}>{this.props.x.name}</a></h3></div>
                <p>Rating: {this.props.x.rating}</p>
                <StarRatings
                    starRatedColor="yellow"
                    rating = {this.props.x.rating}
                    starDimension="40px"
                    starSpacing="5px"
                />
                <p>Reviews:</p>
                <div className = "tweet">
                    {this.state.showMore? this.props.x.tweets.map((y)=>
                    <p><i>"{y[0]}" -@{y[1]}</i></p>) : this.props.x.tweets.slice(0, 2).map((y)=>
                        <p><i>"{y[0]}" -@{y[1]}</i></p>)   
                    }
                </div>
                <Button onClick={this.toggle}>Toogle More Reviews</Button>
            </Card>
		)
	}
	
	
}

export default MyCard;

/*
	componentDidMount(){
		console.log("Hey what's up b")
		const url="/books"
		fetch(url)
			.then((data)=>data.json())
			.then((data)=>{this.setState({books:data})})
	}
*/