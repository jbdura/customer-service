import React, { useEffect, useState } from 'react';

function Customers () {
  const URL = "http://localhost:8000/api/accounts/customers/";

  const [ customer, setCustomer ] = useState( [] );

  useEffect( () => {
    fetch( URL )
      .then( ( res ) => res.json() )
      .then( ( data ) => {
        console.log( data );

        // Ensure data.results is an array before setting the state
        const customerArray = Array.isArray( data.results ) ? data.results : [];

        setCustomer( data );
      } );
  }, [] );

  return (
    <div className="mx-auto max-w-6xl">
      <h2 className="text-2xl font-bold mb-4">List of Customers</h2>
      <table className="min-w-full bg-white border border-gray-300">
        <thead>
          <tr>
            <th className="py-2 px-4 border-b">Customer Name</th>
          </tr>
        </thead>
        <tbody>
          { customer.map( ( customer ) => (
            <tr key={ customer.id }>
              <td className="py-2 px-4 border-b">{ customer.name }</td>
            </tr>
          ) ) }
        </tbody>
      </table>
    </div>
  );
}

export default Customers;


// import React, { useEffect, useState } from 'react';

// function customer() {
//   const URL = "http://localhost:8000/api/accounts/customer/";

//   const [customer, setCustomer] = useState([]);

//   useEffect(() => {
//     fetch(URL)
//       .then((res) => res.json())
//       .then((data) => {
//         console.log(data);
//         setCustomer(data.results);
//       });
//   }, []);

//   return (
//     <div className="mx-auto max-w-6xl">
//       <h2 className="text-2xl font-bold mb-4">List of customer</h2>
//       <table className="min-w-full bg-white border border-gray-300">
//         <thead>
//           <tr>
//             <th className="py-2 px-4 border-b">Agent Name</th>
//           </tr>
//         </thead>
//         <tbody>
//           {customer.map((agentreq) => (
//             <tr key={agentreq.id}>
//               <td className="py-2 px-4 border-b">{agentreq}</td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </div>
//   );
// }

// export default customer;

// import React, { useEffect, useState } from 'react'
// // import MovieList from './movieList';

// function customer () {

//   const URL = "http://localhost:8000/api/accounts/customer/"

//   const [ customer, setCustomer ] = useState( [] );
//   // const example=['one','two']

//   useEffect( () => {
//     fetch( URL )
//       .then( ( res ) => res.json() )
//       .then( data => {
//         console.log( data )
//         setCustomer( data.results )
//       } )
//   }, [] )

//   return (
//     <div className="mx-auto max-w-6xl flex items-center justify-center">
//       <div className="sm:grid sm:grid-cols md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
//         {/* { customer.map( ( moviereq ) =>
//           <MovieList key={ moviereq.id } { ...moviereq } /> ) } */}
//       </div>

//     </div>
//   )
// }

// export default customer;

