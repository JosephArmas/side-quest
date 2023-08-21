import quasiChillin from "../images/quasimoto-lord-quas.gif";
import supremeJacket from "../images/supreme.png";
import bapeJacket from "../images/bape-tiger.png"
import stussyJacket from "../images/stussy.png"
import fuctJacket from "../images/fuct.png"
import quasiShirt from "../images/mvxquasi.png"
import publicQuasi from "../images/public_enemy_edited.png" 
import xLHoodie from "../images/x-large-hoodie.png"
import dilla from "../images/dilla_shirt.png"
import Card from "./Card";
export default Featured;
function Featured() {
  return (
    <>
      <div className="conatiner relative h-screen">
        <img src={quasiChillin} className="w-full h-screen absolute z-0" />
        <div className="grid grid-rows-2 grid-cols-4 gap-10 absolute inset-0 z-10 px-10">
          <Card image={supremeJacket} title="Supreme Skeleton" />
          <Card image={bapeJacket} title="Bape Tiger Shark" />
          <Card image={stussyJacket} title="Stussy Jacket" />
          <Card image={fuctJacket} title="Fuct Jacket" />
          <Card image={xLHoodie} title="XLarge Hoode" />
          <Card image={quasiShirt} title="Quasimoto x Madvillain" />
          <Card image={publicQuasi} title="Quasimoto x Public Enemy" />
          <Card image={dilla} title="Stussy x JDilla" />

        </div>
      </div>
    </>
  );
}
