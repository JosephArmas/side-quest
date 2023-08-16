export default Services
function Services() {

  return(
  <div className="conatiner-services">
    <h1 className="text-3xl text-center pt-20 font-bold">Services</h1>
    <div className="flex flex-row justify-center p-10 space-x-5">
      <div>
        <div className="badge badge-primary badge-lg">Services 1</div>
        <p className="p-2">Description of service 1</p>
      </div>
      <div>
        <div className="badge badge-primary badge-lg">Services 2</div>
        <p className="p-2">Description of service 2</p>
      </div>
      <div>
        <div className="badge badge-primary badge-lg ">Services 3</div>
        <p className="p-2">Description of service 3</p>
      </div>
    </div>
  </div>

  );
}
