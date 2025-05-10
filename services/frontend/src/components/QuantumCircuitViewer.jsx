import { Canvas } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import * as THREE from 'three'
import anime from 'animejs'

export default function QuantumCircuitViewer({ qubits, entanglement }) {
  return (
    <Canvas camera={{ position: [0, 10, 15], fov: 50 }}>
      <ambientLight intensity={0.5} />
      <pointLight position={[10, 10, 10]} />
      
      {/* Qubit Spheres */}
      {qubits.map((state, i) => (
        <QubitSphere 
          key={i}
          position={[i * 3 - qubits.length/2, 0, 0]}
          state={state}
        />
      ))}
      
      {/* Entanglement Lines */}
      {entanglement.map(([q1, q2], idx) => (
        <EntanglementLine
          key={idx}
          start={[q1 * 3 - qubits.length/2, 0, 0]}
          end={[q2 * 3 - qubits.length/2, 0, 0]}
        />
      ))}
      
      <OrbitControls enableZoom={true} />
    </Canvas>
  )
}