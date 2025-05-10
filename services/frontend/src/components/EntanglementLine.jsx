import { Line } from '@react-three/drei'
import { useMemo } from 'react'
import * as THREE from 'three'
import anime from 'animejs'

export function EntanglementLine({ start, end }) {
  const points = useMemo(() => {
    const curve = new THREE.LineCurve3(
      new THREE.Vector3(...start),
      new THREE.Vector3(...end)
    )
    return curve.getPoints(50)
  }, [start, end])

  // Animate entanglement effect
  useEffect(() => {
    anime({
      targets: { progress: 0 },
      progress: 1,
      duration: 2000,
      loop: true,
      easing: 'linear',
      update: anim => {
        const visiblePoints = Math.floor(points.length * anim.progress)
        setVisiblePoints(points.slice(0, visiblePoints))
      }
    })
  }, [])

  return (
    <Line
      points={points}
      color="cyan"
      lineWidth={2}
      dashed={true}
      dashSize={0.2}
      gapSize={0.1}
    />
  )
}