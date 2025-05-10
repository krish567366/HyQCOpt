import { useFrame } from '@react-three/fiber'
import { Sphere } from '@react-three/drei'
import { useRef, useEffect } from 'react'
import * as THREE from 'three'
import anime from 'animejs'

export function QubitSphere({ position, state }) {
  const meshRef = useRef()
  const materialRef = useRef()
  const scale = state === '1' ? 1.2 : 1

  // State change animation
  useEffect(() => {
    anime({
      targets: meshRef.current.scale,
      x: scale,
      y: scale,
      z: scale,
      duration: 800,
      easing: 'easeOutElastic(1, .5)'
    })
    
    anime({
      targets: materialRef.current.color,
      r: state === '1' ? 1 : 0.2,
      g: state === '1' ? 0.2 : 0.6,
      b: state === '1' ? 0.2 : 1,
      duration: 1000
    })
  }, [state])

  return (
    <Sphere ref={meshRef} position={position} args={[0.8, 32, 32]}>
      <meshStandardMaterial 
        ref={materialRef} 
        color={new THREE.Color(0.2, 0.6, 1)}
        metalness={0.3}
        roughness={0.2}
      />
    </Sphere>
  )
}