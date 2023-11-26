import React, { useEffect, useState } from 'react';

function Messages () {
  const MessageURL = "http://localhost:8000/api/messaging/messages/";
  const ResponseURL = "http://localhost:8000/api/messaging/responses/";
  const AgentsURL = "http://localhost:8000/api/accounts/agents/";

  const [ messages, setMessages ] = useState( [] );
  const [ agents, setAgents ] = useState( [] );
  const [ selectedAgent, setSelectedAgent ] = useState( null );

  useEffect( () => {
    fetch( MessageURL )
      .then( ( res ) => res.json() )
      .then( ( data ) => {
        console.log( data );
        setMessages( data );
      } );

    fetch( AgentsURL )
      .then( ( res ) => res.json() )
      .then( ( data ) => {
        console.log( data );
        setAgents( data ); // Assuming agents are in data.
      } );
  }, [] );

  const handleSubmit = ( messageId, agentReplyContent ) => {
    // Check if an agent is selected
    if ( !selectedAgent ) {
      console.error( 'Please select an agent' );
      return;
    }

    // Create a new response object
    const newResponse = {
      content: agentReplyContent,
      timestamp: new Date().toISOString(),
      agent: selectedAgent.id,
      message: messageId,
    };

    // Send a POST request to save the response
    fetch( ResponseURL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify( newResponse ),
    } )
      .then( ( res ) => res.json() )
      .then( ( data ) => {
        console.log( 'Response saved:', data );
      } )
      .catch( ( error ) => {
        console.error( 'Error saving response:', error );
      } );
  };

  return (
    <div className="mx-auto max-w-6xl">
      <h2 className="text-2xl font-bold mb-4">List of Messages</h2>
      { messages.map( ( message ) => (
        <div key={ message.id } className="bg-white border border-gray-300 p-4 mb-4 rounded">
          <h3 className="text-xl font-bold mb-2">{ message.customer.name }</h3>
          <p>{ message.content }</p>
          <form
            onSubmit={ ( e ) => {
              e.preventDefault();
              const agentReplyContent = e.target.elements.replyContent.value;
              handleSubmit( message.id, agentReplyContent );
            } }
          >
            <label className="block mt-4">
              Answer:
              <textarea
                name="replyContent"
                className="form-textarea mt-1 block w-full"
                rows="3"
                placeholder="Type your reply here..."
              />
            </label>
            <label className="block mt-4">
              Select Agent:
              <select
                name="agent"
                className="form-select mt-1 block w-full"
                onChange={ ( e ) => setSelectedAgent( JSON.parse( e.target.value ) ) }
              >
                <option value="" disabled selected>
                  Select an agent
                </option>
                { agents.map( ( agent ) => (
                  <option key={ agent.id } value={ JSON.stringify( agent ) }>
                    { agent.name }
                  </option>
                ) ) }
              </select>
            </label>
            <button
              type="submit"
              className="mt-4 bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-700"
            >
              Submit Reply
            </button>
          </form>
        </div>
      ) ) }
    </div>
  );
}

export default Messages;



// import React, { useEffect, useState } from 'react';

// function Messages () {
//   const MessageURL = "http://localhost:8000/api/messaging/messages/";
//   const ResponseURL = "http://localhost:8000/api/messaging/responses/";
//   const AgentsURL = "http://localhost:8000/api/accounts/agents/";


//   const [ messages, setMessages ] = useState( [] );

//   useEffect( () => {
//     fetch( MessageURL )
//       .then( ( res ) => res.json() )
//       .then( ( data ) => {
//         console.log( data );

//         // Ensure data.results is an array before setting the state

//         setMessages( data );
//       } );
//   }, [] );

//   const handleSubmit = ( messageId, agentReplyContent ) => {
//     // Create a new response object
//     const newResponse = {
//       content: agentReplyContent,
//       timestamp: new Date().toISOString(), // You can format this date based on your preference
//       agent: 1, // Replace with the actual agent ID
//       message: messageId,
//     };

//     // Send a POST request to save the response
//     fetch( ResponseURL, {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify( newResponse ),
//     } )
//       .then( ( res ) => res.json() )
//       .then( ( data ) => {
//         console.log( 'Response saved:', data );
//         // You might want to update the state or perform other actions after saving the response
//       } )
//       .catch( ( error ) => {
//         console.error( 'Error saving response:', error );
//         // Handle errors as needed
//       } );
//   };

//   return (
//     <div className="mx-auto max-w-6xl">
//       <h2 className="text-2xl font-bold mb-4">List of Messages</h2>
//       { messages.map( ( message ) => (
//         <div key={ message.id } className="bg-white border border-gray-300 p-4 mb-4 rounded">
//           <h3 className="text-xl font-bold mb-2">{ message.customer.name }</h3>
//           <p>{ message.content }</p>
//           <form
//             onSubmit={ ( e ) => {
//               e.preventDefault();
//               const agentReplyContent = e.target.elements.replyContent.value;
//               handleSubmit( message.id, agentReplyContent );
//             } }
//           >
//             <label className="block mt-4">
//               Answer:
//               <textarea
//                 name="replyContent"
//                 className="form-textarea mt-1 block w-full"
//                 rows="3"
//                 placeholder="Type your reply here..."
//               />
//             </label>
//             <button
//               type="submit"
//               className="mt-4 bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-700"
//             >
//               Submit Reply
//             </button>
//           </form>
//         </div>
//       ) ) }
//     </div>
//   );
// }

// export default Messages;


// import React, { useEffect, useState } from 'react';

// function Messages () {
//   const MessageURL = "http://localhost:8000/api/messaging/messages/";
//   const AgentsURL = "http://localhost:8000/api/accounts/agents/";

//   const [ messages, setMessages ] = useState( [] );

//   useEffect( () => {
//     fetch( MessageURL )
//       .then( ( res ) => res.json() )
//       .then( ( data ) => {
//         console.log( data );

//         // Ensure data.results is an array before setting the state

//         setMessages( data );
//       } );
//   }, [] );

//   return (
//     <div className="mx-auto max-w-6xl">
//       <h2 className="text-2xl font-bold mb-4">List of Messages</h2>
//       { messages.map( ( message ) => (
//         <div key={ message.id } className="bg-white border border-gray-300 p-4 mb-4 rounded">
//           <h3 className="text-xl font-bold mb-2">{ message.customer.name }</h3>
//           <p>{ message.content }</p>
//           <form>
//             <label className="block mt-4">
//               Answer:
//               <textarea
//                 className="form-textarea mt-1 block w-full"
//                 rows="3"
//                 placeholder="Type your reply here..."
//               />
//             </label>
//             <button
//               type="submit"
//               className="mt-4 bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-700"
//             >
//               Submit Reply
//             </button>
//           </form>
//         </div>
//       ) ) }
//     </div>
//   );
// }

// export default Messages;


// import React, { useEffect, useState } from 'react';

// function Messages () {
//   const URL = "http://localhost:8000/api/messaging/messages/";

//   const [ message, setMessage ] = useState( [] );

//   useEffect( () => {
//     fetch( URL )
//       .then( ( res ) => res.json() )
//       .then( ( data ) => {
//         console.log( data );

//         // Ensure data.results is an array before setting the state
//         // const messageArray = Array.isArray( data.results ) ? data.results : [];

//         setMessage( data );
//       } );
//   }, [] );

//   return (
//     <div className="mx-auto max-w-6xl">
//       <h2 className="text-2xl font-bold mb-4">List of messages</h2>
//       <table className="min-w-full bg-white border border-gray-300">
//         <thead>
//           <tr>
//             <th className="py-2 px-4 border-b">Messages</th>
//           </tr>
//         </thead>
//         <tbody>
//           { message.map( ( message ) => (
//             <tr key={ message.id }>
//               <td className="py-2 px-4 border-b">{ message.name }</td>
//             </tr>
//           ) ) }
//         </tbody>
//       </table>
//     </div>
//   );
// }

// export default Messages;
