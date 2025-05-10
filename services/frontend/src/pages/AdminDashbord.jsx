// services/frontend/src/pages/AdminDashboard.jsx
import { useWebSocket } from 'react-use-websocket';

const AdminDashboard = () => {
  const [metrics, setMetrics] = useState({});
  const { lastMessage } = useWebSocket('wss://api.hyqcopt.com/ws/admin');

  useEffect(() => {
    if (lastMessage) {
      setMetrics(JSON.parse(lastMessage.data));
    }
  }, [lastMessage]);

  return (
    <div className="grid grid-cols-4 gap-4">
      <QuantumHardwareStatus metrics={metrics.quantum} />
      <JobQueueChart data={metrics.jobs} />
      <UserManagementTable />
      <ComplianceControls />
    </div>
  );
};