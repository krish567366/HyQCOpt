// services/frontend/src/components/WebGLCircuitViewer.jsx
import { Canvas } from '@react-three/fiber'

const CircuitViewer = ({ qubits }) => {
  return (
    <Canvas camera={{ position: [0, 0, 10] }}>
      <ambientLight intensity={0.5} />
      {Array.from({ length: qubits }).map((_, i) => (
        <QubitLine key={i} position={[i * 1.5 - qubits/2, 0, 0]} />
      ))}
    </Canvas>
  );
};