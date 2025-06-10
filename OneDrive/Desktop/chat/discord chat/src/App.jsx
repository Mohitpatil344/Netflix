// import TelegramWidget from './TelegramWidget';
import DiscordWidget from './DiscordChatWidget';

function App() {
  return (
    <div>
      {/* <h1>My Telegram Channel</h1>
      <TelegramWidget /> */}
      <h1>My Discord Channel</h1>
      <h2>Join Discord Community</h2>
      <h2>
        Tap on:{" "}
        <a href="https://discord.gg/HNevSdkF" target="_blank" rel="noopener noreferrer">
          https://discord.gg/HNevSdkF
        </a>
      </h2>
      <DiscordWidget />
    </div>
  );
}

export default App;
