async function fetchMTAData() {
  try {
    const response = await fetch('http://127.0.0.1:5000/getMTAData');
    const mtaData = await response.json();
    return mtaData;
  } catch (error) {
    console.error('Error fetching MTA data:', error);
    throw error; 
  }
}

function dijkstra(graph, start, goal) {
  let shortestDistance = {};
  let predecessor = {};
  let path = [];
  let unseen = Object.keys(graph);
  let INFINITY = 9999999;

  unseen.forEach(node => {
      shortestDistance[node] = INFINITY;
  });
  shortestDistance[start] = 0;

  while (unseen.length > 0) {
      let minNode = null;

      unseen.forEach(node => {
          if (minNode === null) {
              minNode = (node.slice(0, 2) === "N " || node.slice(0, 2) === "S ") ? node.slice(2) : node;
          } else if (shortestDistance[node] < shortestDistance[minNode]) {
              minNode = (node.slice(0, 2) === "N " || node.slice(0, 2) === "S ") ? node.slice(2) : node;
          }
      });

      for (let [childNode, weight] of Object.entries(graph[minNode])) {
          childNode = (childNode.slice(0, 2) === "N " || childNode.slice(0, 2) === "S ") ? childNode.slice(2) : childNode;
          if (weight + shortestDistance[minNode] < shortestDistance[childNode]) {
              shortestDistance[childNode] = weight + shortestDistance[minNode];
              predecessor[childNode] = minNode;
          }
      }

      unseen = unseen.filter(node => node !== minNode);
  }

  let currentNode = goal;
  while (currentNode !== start) {
      try {
          path.unshift(currentNode);
          currentNode = predecessor[currentNode];
      } catch (e) {
          console.log('Path not reachable');
          break;
      }
  }
  path.unshift(start);

  if (shortestDistance[goal] !== INFINITY) {
    console.log(`Shortest distance is ${Math.floor(shortestDistance[goal] / 60)} minutes`);
    console.log(`And the path is`);
    document.querySelector('.time').innerText = `Shortest distance is ${Math.floor(shortestDistance[goal] / 60)} minutes`;
    let pathsText = ''; // Variable to store concatenated paths
    
    for (let i = 0; i < path.length; i++) {
        console.log(path[i]);
        pathsText += path[i] + '\n'; // Concatenate paths with a newline
    }
    document.querySelector('.path').innerText = `And the path is`;
    document.querySelector('.result').innerText = pathsText; // Update the HTML element with all paths
}

}

export async function runDijkstra(start, end) {
  try {
    const stopsGraph = await fetchMTAData();

    dijkstra(stopsGraph, start, end);
  } catch (error) {
    console.error('Error:', error);
  }
}

// runDijkstra('168 St-Washington Hts', 'Whitlock Av');