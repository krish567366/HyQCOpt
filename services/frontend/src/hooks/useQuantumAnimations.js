import { useEffect } from 'react'
import anime from 'animejs'

export function useQuantumAnimations(circuitState) {
  useEffect(() => {
    // Global loading animation
    const loader = anime({
      targets: '.quantum-loader',
      rotate: 360,
      duration: 1500,
      loop: true,
      easing: 'linear',
      autoplay: false
    })
    
    // State-dependent animations
    const stateAnimations = {
      processing: () => {
        loader.play()
        anime({
          targets: '.quantum-node',
          opacity: [0.5, 1],
          duration: 800,
          easing: 'easeInOutQuad',
          loop: true,
          direction: 'alternate'
        })
      },
      completed: () => {
        loader.pause()
        anime({
          targets: '.quantum-result',
          scale: [0.9, 1],
          opacity: [0, 1],
          duration: 1200,
          easing: 'easeOutElastic(1, .5)'
        })
      }
    }
    
    circuitState && stateAnimations[circuitState]?.()
    
    return () => {
      loader.pause()
      anime.remove('.quantum-node, .quantum-result')
    }
  }, [circuitState])
}