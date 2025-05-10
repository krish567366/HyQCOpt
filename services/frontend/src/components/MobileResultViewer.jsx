// services/frontend/src/components/MobileResultViewer.jsx
const MobileResultView = ({ results }) => {
  const [activeTab, setActiveTab] = useState('summary');

  return (
    <div className="block lg:hidden">
      <Tabs value={activeTab}>
        <Tab value="summary" onClick={() => setActiveTab('summary')}>
          Summary
        </Tab>
        <Tab value="details" onClick={() => setActiveTab('details')}>
          Details
        </Tab>
      </Tabs>
      
      <SwipeableViews index={activeTab === 'summary' ? 0 : 1}>
        <ResultSummary data={results} />
        <DetailedMetrics data={results} />
      </SwipeableViews>
    </div>
  );
};