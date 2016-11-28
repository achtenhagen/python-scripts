<?php

	/* Stocks HW9 */

	# Open database connection
	$db = new mysqli("127.0.0.1", "root", "", "stocks");
	$db->set_charset('utf8');
	if ($db->connect_errno) {
		header($_SERVER['SERVER_PROTOCOL'] . ' 500 Internal Server Error');
		exit();
	}
	# Read stocks from database
	$stocks = [];
	$query = "SELECT rank,title,volume,price,diff,perc_diff FROM `2016-11-28`";
	if ($stmt = $db->prepare($query)) {
		$stmt->execute();
		$result = $stmt->get_result();
		$stmt->free_result();
		$stmt->close();
		while ($row = $result->fetch_array(MYSQLI_ASSOC)) {
			$stocks[] = [
				"rank"      => $row['rank'],
				"title"     => $row['title'],
				"volume"    => $row['volume'],
				"price"     => $row['price'],
				"diff"      => $row['diff'],
				"perc_diff" => $row['perc_diff']
			];
		}
		# print_r($stocks);		
	}
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Stocks</title>
		<style>
			* {
				border: 0;
				box-sizing: border-box;
				-moz-box-sizing: border-box;
				-webkit-box-sizing: border-box;
				outline: none;
			}

			body {
				color: #000;
				font-family: 'Arial', Helvetica, sans-serif;
				font-size: 14px;
				height: 100%;
				letter-spacing: 0;
				line-height: 1;
			}

			body, h1, h2, h3, h4, h5, h6, ul {
				margin: 0;
				padding: 0;
			}									
			th { text-align: left }
			th,td { min-width: 100px; padding-left: 10px }
			th:first-child, td:first-child { padding-left: 0; text-align: center }
			thead,tr { height: 30px }
			tr:nth-child(even) { background: rgba(0, 0, 0, .05) }
						
		</style>
	</head>
	<body>
		<table>
			<thead>
				<tr>
					<th>Rank</th>
					<th>Title</th>
					<th>Volume</th>
					<th>Price</th>
					<th>Change</th>
					<th>% Change</th>
				</tr>
			 </thead>
			<?php			
			foreach ($stocks as $stock) {
				echo "<tr>" .
					 "<td>" . $stock['rank'] . "</td>" .
					 "<td>" . $stock['title'] . "</td>" .
					 "<td>" . $stock['volume'] . "</td>" .
					 "<td>" . $stock['price'] . "</td>" .
					 "<td>" . $stock['diff'] . "</td>" .
					 "<td>" . $stock['perc_diff'] . "</td>" .
					"</tr>";
			}			
			?>
		</table>
	</body>
</html>