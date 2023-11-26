import React, { useEffect, useState } from 'react';
import Navbar from '@/components/Navbar';

function Agents () {
  const URL = "http://localhost:8000/api/accounts/agents/";

  const [ agents, setAgents ] = useState( [] );

  useEffect( () => {
    fetch( URL )
      .then( ( res ) => res.json() )
      .then( ( data ) => {
        console.log( data );

        // Ensure data.results is an array before setting the state
        // const agentsArray = Array.isArray( data.results ) ? data.results : [];

        setAgents( data );
      } );
  }, [] );

  return (
    <div>
      <Navbar />
      <div className="mx-auto max-w-6xl">
        <h2 className="text-2xl font-bold mb-4">List of Agents</h2>
        <table className="min-w-full bg-white border border-gray-300">
          <thead>
            <tr>
              <th className="py-2 px-4 border-b">Agent Name</th>
            </tr>
          </thead>
          <tbody>
            { agents.map( ( agent ) => (
              <tr key={ agent.id }>
                <td className="py-2 px-4 border-b">{ agent.name }</td>
              </tr>
            ) ) }
          </tbody>
        </table>
      </div>
    </div>

  );
}

export default Agents;


// import React, { useEffect, useState } from 'react';

// function Agents() {
//   const URL = "http://localhost:8000/api/accounts/agents/";

//   const [agents, setAgents] = useState([]);

//   useEffect(() => {
//     fetch(URL)
//       .then((res) => res.json())
//       .then((data) => {
//         console.log(data);
//         setAgents(data.results);
//       });
//   }, []);

//   return (
//     <div className="mx-auto max-w-6xl">
//       <h2 className="text-2xl font-bold mb-4">List of Agents</h2>
//       <table className="min-w-full bg-white border border-gray-300">
//         <thead>
//           <tr>
//             <th className="py-2 px-4 border-b">Agent Name</th>
//           </tr>
//         </thead>
//         <tbody>
//           {agents.map((agentreq) => (
//             <tr key={agentreq.id}>
//               <td className="py-2 px-4 border-b">{agentreq}</td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </div>
//   );
// }

// export default Agents;

// import React, { useEffect, useState } from 'react'
// // import MovieList from './movieList';

// function Agents () {

//   const URL = "http://localhost:8000/api/accounts/agents/"

//   const [ agents, setAgents ] = useState( [] );
//   // const example=['one','two']

//   useEffect( () => {
//     fetch( URL )
//       .then( ( res ) => res.json() )
//       .then( data => {
//         console.log( data )
//         setAgents( data.results )
//       } )
//   }, [] )

//   return (
//     <div className="mx-auto max-w-6xl flex items-center justify-center">
//       <div className="sm:grid sm:grid-cols md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
//         {/* { agents.map( ( moviereq ) =>
//           <MovieList key={ moviereq.id } { ...moviereq } /> ) } */}
//       </div>

//     </div>
//   )
// }

// export default Agents;

