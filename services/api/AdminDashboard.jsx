import { Canvas } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import { useQuantumMetrics } from '../hooks/useQuantumMetrics'

export default function AdminDashboard() {
  const { qpuStatus, jobs } = useQuantumMetrics()

  return (
    <div className="dashboard">
      <div className="metrics-panel">
        <QuantumGauge metrics={qpuStatus} />
        <JobQueueChart jobs={jobs} />
      </div>
      
      <Canvas className="qpu-visualization">
        <ambientLight intensity={0.5} />
        <QpuModel status={qpuStatus} />
        <OrbitControls enableZoom={true} />
      </Canvas>
    </div>
  )
}