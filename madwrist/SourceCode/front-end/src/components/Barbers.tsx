type BarberProps = {
  barbers: string[];
};
export default Barbers;
function Barbers({ barbers }: BarberProps) {
  return (
    <div className="text-red-700">
      <ul>
        {barbers.map((barber) => (
          <li key={barber}>{barber}</li>
        ))}
      </ul>
    </div>
  );
}
