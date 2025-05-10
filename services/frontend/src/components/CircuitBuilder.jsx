import { useState } from 'react'
import { useQuantumAnimations } from '../hooks/useQuantumAnimations'
import QuantumCircuitViewer from './QuantumCircuitViewer'

export default function CircuitBuilder() {
  const [qubits, setQubits] = useState(Array(5).fill('0'))
  const [entanglement, setEntanglement] = useState([[0, 1], [1, 2]])
  const [circuitState, setCircuitState] = useState(null)

  useQuantumAnimations(circuitState)

  const addGate = (gate, qubitIndex) => {
    setQubits(q => 
      q.map((v, i) => i === qubitIndex ? (v === '0' ? '1' : '0') : v)
    )
    
    anime({
      targets: `.qubit-${qubitIndex}`,
      positionY: '+=1',
      duration: 800,
      direction: 'alternate',
      easing: 'easeInOutQuad'
    })
  }

  return (
    <div className="circuit-builder">
      <div className="quantum-loader" />
      
      <div className="controls">
        {qubits.map((_, i) => (
          <button 
            key={i}
            className={`quantum-node qubit-${i}`}
            onClick={() => addGate('X', i)}
          >
            Qubit {i+1}
          </button>
        ))}
      </div>
      
      <QuantumCircuitViewer 
        qubits={qubits}
        entanglement={entanglement}
      />
      
      <button 
        className="quantum-result"
        onClick={() => setCircuitState('processing')}
      >
        Run Quantum Circuit
      </button>
    </div>
  )
}