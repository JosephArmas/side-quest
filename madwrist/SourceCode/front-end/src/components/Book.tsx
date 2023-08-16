import { useState } from 'react';
import Calendar from 'react-calendar'


type BookProps = {
  message?: string
}

export default function Book({message}: BookProps)
{
  const [showCalendar, setShowCalendar] = useState(false);
  // const [value,onChange] = useState(new Date());

  function clickHandler()
  {
    setShowCalendar(prevState => !prevState);
  }

  return(
  <div className="text-center pt-20">
      {/* <button className="rounded-full bg-sky-500 w-40 " onClick={clickHandler}>Book Appointment</button> */}
      <button className="btn btn-outline text-lg place-content-center" onClick={clickHandler}>Book Appointment</button>
      {showCalendar && 
        <div className="flex justify-center items-center p-2">
          <Calendar />
        </div>
      }
      {/* <Calendar onChange={onChange} value={value}/> */}
  </div>
  )

}


// function clickHandler()
// {
//   alert("hello")
// }
