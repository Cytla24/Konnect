import React from "react";
import "@blueprintjs/core";
import "@blueprintjs/core/lib/css/blueprint.css";
import "@blueprintjs/icons/lib/css/blueprint-icons.css";
import { Button, Card, Elevation } from "@blueprintjs/core";
import StarRatings from "react-star-ratings";
import "./Konnect.css";

class MyCard extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			showMore: false,
		};
		this.toggle = this.toggle.bind(this);
	}

	render() {
		const {
			data: { name, link, rating, tweets },
		} = this.props;
		return (
			<Card interactive={true} elevation={Elevation.TWO}>
				<div className="bp3-icon-share name-header">
					<h3>
						<a href={link || `https://www.google.com/?q=${name}`}>{name}</a>
					</h3>
				</div>
				<p>Rating: {rating}</p>
				<StarRatings
					starRatedColor="yellow"
					rating={rating}
					starDimension="40px"
					starSpacing="5px"
				/>
				<p>Reviews:</p>
				<div className="tweet">
					{this.state.showMore
						? tweets.map((tweet) => (
								<p>
									<i>
										"{tweet[0]}" -@{tweet[1]}
									</i>
								</p>
						  ))
						: tweets.slice(0, 2).map((tweet) => (
								<p>
									<i>
										"{tweet[0]}" -@{tweet[1]}
									</i>
								</p>
						  ))}
				</div>
				<Button onClick={this.toggle}>Toogle More Reviews</Button>
			</Card>
		);
	}

	toggle() {
		if (this.state.showMore) {
			this.setState({ showMore: false });
		} else {
			this.setState({ showMore: true });
		}
	}
}

export default MyCard;
