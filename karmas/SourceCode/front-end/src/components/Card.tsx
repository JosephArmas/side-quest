type CardProps = {
  image: string
  title: string

}
export default Card
function Card(prop: CardProps) {
  return (
  <>
          <div className="card w-96 relative transition-all duration-300 hover:opacity-100"
          onMouseOver={(e) => {
              const imgElement = e.currentTarget.children[0] as HTMLImageElement;
              const contentElement = e.currentTarget.children[1] as HTMLDivElement;
              imgElement.style.opacity = "0";
              contentElement.style.opacity = "1";
            }}
            onMouseOut={(e) => {
              const imgElement = e.currentTarget.children[0] as HTMLImageElement;
              const contentElement = e.currentTarget.children[1] as HTMLDivElement;
              imgElement.style.opacity = "1";
              contentElement.style.opacity = "0";

            }}
          >
            <img
              src={prop.image}
              className="w-full h-full transition-all duration-300 opacity-100"
              style = {{transition: 'all 0.3s', opacity: '1'}}
            />
            <div className="card-content absolute inset-0 flex flex-col justify-center items-center text-center transition-all duration-300"
              style = {{ transition: 'all 0.3s', opacity: '0'}}
            >
              <h2 className="card-title text-black ">{prop.title}</h2>
              <div className="card-actions justify-end p-4">
                <button className="btn btn-primary">Buy Now</button>
              </div>
            </div>
          </div>
  </>

  )
}
