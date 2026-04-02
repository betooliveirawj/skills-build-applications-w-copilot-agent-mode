import { render, screen } from '@testing-library/react';
import App from './App';

test('renders OctoFit Tracker header', () => {
  render(<App />);
  const linkElement = screen.getByText(/OctoFit Tracker/i);
  expect(linkElement).toBeInTheDocument();
});
